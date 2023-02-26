from __future__ import print_function

import os.path
from google.oauth2.credentials import Credentials
from google_auth_httplib2 import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def create_service():
    SCOPES = ['https://www.googleapis.com/auth/calendar.app.created',  # TODO: check if this is needed
              'https://www.googleapis.com/auth/calendar.calendarlist.readonly',
              'https://www.googleapis.com/auth/calendar.events.freebusy',
              'https://www.googleapis.com/auth/calendar.events.public.readonly',
              'https://www.googleapis.com/auth/calendar.settings.readonly',
              'https://www.googleapis.com/auth/calendar.freebusy']
    creds = None

    token_path = 'resources/token.json'
    credentials_path = 'resources/credentials.json'

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists(token_path):  # TODO: nie sprawdzamy tokena bo go nie ma
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)


            # Save the credentials for the next run TODO:nie tworzymy tokena na przyszłość
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        print('User authorized')
        return service

    except HttpError as error:
        print('An error occurred: %s' % error)
