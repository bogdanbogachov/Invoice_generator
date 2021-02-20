from __future__ import print_function
import datetime
import pickle
import os.path
from interface import customer
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

name = customer

start_time = None
end_time = None
place = None
summary = None

# finding the current folder path
folder = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(folder, "credentials.json")

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials_path', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    before = (datetime.datetime.now() - datetime.timedelta(1)).isoformat() + 'Z' # 'Z' indicates UTC time
    after = (datetime.datetime.now() + datetime.timedelta(2)).isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=before,
                                        timeMax=after,
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        pass
    for event in events:
        if event['summary'] == f"{name}":
            global start_time
            start_time = event['start'].get('dateTime', event['start'].get('date'))
            start_time = start_time[11:-9]
            global end_time
            end_time = event['end'].get('dateTime', event['end'].get('date'))
            end_time = end_time[11:-9]
            global location
            location = event['location']
            global summary
            summary = event['summary']