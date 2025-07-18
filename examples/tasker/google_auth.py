import os
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']


def get_google_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def get_drive_files(creds, query: str):

    drive_service = build('drive', 'v3', credentials=creds)
    page_token = None

    results = drive_service.files().list(
        # q=f"trashed = false and name = 'reverse proxy.drawio'",
        q=query,
        fields='nextPageToken, files(name, webViewLink, mimeType)',
        pageToken=page_token
    ).execute()

    items = results.get('files', [])

    return items
