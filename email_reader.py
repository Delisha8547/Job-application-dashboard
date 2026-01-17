from googleapiclient.discovery import build
import base64

# Add unwanted senders or domains here
UNWANTED_SENDERS = ["no-reply@quora.com", "info@quora.com", "digest@quora.com"]

def extract_body(payload):
    body = ""

    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain' and part['body'].get('data'):
                body += base64.urlsafe_b64decode(
                    part['body']['data']
                ).decode('utf-8', errors='ignore')
            elif part['mimeType'] == 'text/html' and part['body'].get('data'):
                body += base64.urlsafe_b64decode(
                    part['body']['data']
                ).decode('utf-8', errors='ignore')
            elif 'parts' in part:
                body += extract_body(part)
    else:
        if payload['body'].get('data'):
            body += base64.urlsafe_b64decode(
                payload['body']['data']
            ).decode('utf-8', errors='ignore')

    return body

def get_job_emails(creds):
    service = build('gmail', 'v1', credentials=creds)

    # Your original query for job-related emails
    query = "application OR interview OR assessment OR unfortunately OR regret OR unsuccessful"
    results = service.users().messages().list(
        userId='me', q=query, maxResults=30
    ).execute()

    messages = results.get('messages', [])
    emails = []

    for msg in messages:
        message = service.users().messages().get(
            userId='me', id=msg['id'], format='full'
        ).execute()

        payload = message['payload']
        headers = payload.get('headers', [])

        subject = sender = ""
        for h in headers:
            if h['name'] == 'Subject':
                subject = h['value']
            if h['name'] == 'From':
                sender = h['value']

        # Skip unwanted senders
        if any(unwanted in sender for unwanted in UNWANTED_SENDERS):
            continue

        body = extract_body(payload)
        if 'parts' in payload:
            data = payload['parts'][0]['body'].get('data')
            if data:
                body = base64.urlsafe_b64decode(data).decode('utf-8')

        emails.append({
            "subject": subject,
            "sender": sender,
            "body": body
        })

    return emails
