import os
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import models

SCOPES = ['https://www.googleapis.com/auth/drive.readonly',
          'https://www.googleapis.com/auth/calendar.events.owned']


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


def get_drive_files(query: str, creds):

    drive_service = build('drive', 'v3', credentials=creds)
    page_token = None

    results = drive_service.files().list(
        q=query,
        fields='nextPageToken, files(id, name, webViewLink, mimeType)',
        pageToken=page_token
    ).execute()

    items = results.get('files', [])

    return items


def get_drive_file_by_id(file_id: str, creds):
    drive_service = build('drive', 'v3', credentials=creds)
    file = drive_service.files().get(fileId=file_id).execute()
    return file


def create_calendar_event(event_creation_details: models.EventCreationModel, creds, attachments: list[models.EventAttachmentModel] = []):

    calendar_service = build("calendar", "v3", credentials=creds)

    event = event_creation_details.model_dump()
    # files = [get_drive_file_by_id(attachment.fileId, creds)
    #          for attachment in attachments]
    # print(files)
    # event['attachments'] = [{
    #     'fileUrl': file['alternateLink'],
    #     'mimeType': file['mimeType'],
    #     'title': file['title']
    # } for file in files]
    event['attachments'] = [att.model_dump() for att in attachments]

    event_creation_response = calendar_service.events().insert(
        calendarId='primary', body=event).execute()

    return event_creation_response
