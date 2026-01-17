from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
if "RENDER" in os.environ:
    REDIRECT_URI = "https://job-application-dashboardd.onrender.com/oauth2callback"
else:
    REDIRECT_URI = "http://127.0.0.1:8000/oauth2callback"


def get_flow():
    return Flow.from_client_secrets_file(
        'credentials.json',
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )

def save_credentials(creds):
    with open('token.json', 'w') as f:
        f.write(creds.to_json())

def load_credentials():
    if os.path.exists('token.json'):
        return Credentials.from_authorized_user_file('token.json', SCOPES)
    return None



