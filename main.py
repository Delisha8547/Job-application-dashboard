from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from auth import get_flow, save_credentials, load_credentials
from email_reader import get_job_emails
from classifier import classify_email
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app = FastAPI()

# Serve frontend
# Home route
@app.get("/")
def home():
    try:
        return HTMLResponse(open("index.html").read())
    except FileNotFoundError:
        return HTMLResponse("<h1>Index file not found. Make sure frontend/index.html exists</h1>")

# Login route
@app.get("/login")
def login():
    flow = get_flow()
    auth_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    # Redirect user to Google OAuth
    return RedirectResponse(auth_url)

# OAuth callback route
@app.get("/oauth2callback")
def oauth2callback(request: Request):
    flow = get_flow()
    flow.fetch_token(authorization_response=str(request.url))
    creds = flow.credentials
    save_credentials(creds)
    # Redirect to dashboard
    return RedirectResponse(url="/")

# Analyze emails route
@app.get("/analyze")
def analyze_emails():
    creds = load_credentials()
    if not creds:
        # Not logged in yet → return empty data
        summary = {"Rejected": 0, "Assessment": 0, "Interview": 0, "No Response": 0}
        results = []
        return JSONResponse(content={"summary": summary, "applications": results})

    emails = get_job_emails(creds)
    summary = {"Rejected": 0, "Assessment": 0, "Interview": 0, "No Response": 0}
    results = []

    for email in emails:
        status = classify_email(email["body"])
        summary[status] += 1
        company = email["sender"].split("@")[-1] if "@" in email["sender"] else "Unknown"
        results.append({"company": company, "status": status})

    return JSONResponse(content={"summary": summary, "applications": results})
