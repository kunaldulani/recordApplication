from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle, datefinder
from datetime import datetime, timedelta

# Startup function to obtain token credentials
def startup():
    # Set scope for the application.
    # These are the permissions available to this application.
    scopes = ['https://www.googleapis.com/auth/calendar']

    # Create flow and get credentials.
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    credentials = flow.run_console()

    # Save credentials to pickle to avoid authorizing every time.
    pickle.dump(credentials, open("token.pkl", "wb"))


# This method creates an event
# uses datefinder library
def create_event(start_time_str, summary, duration=1,attendees=None, description=None, location=None):
    # Read saved credentials
    credentials = pickle.load(open("token.pkl", "rb"))

    # Create service object
    service = build("calendar", "v3", credentials=credentials)

    # List the calendars.
    # result = service.calendarList().list().execute()
    # 2ar4us2tjh6if8dmm5babjqbpk@group.calendar.google.com
    calendar_id = "2ar4us2tjh6if8dmm5babjqbpk@group.calendar.google.com"
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)

    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': "America/Denver",
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': "America/Denver",
        },
        'attendees': [
        {'email':attendees },
    ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    return service.events().insert(calendarId='primary', body=event,sendNotifications=True).execute()

def addToCalendar(self):
    # Create an event by calling the above mehtod
    create_event('31 May 9.30pm', "Test Meeting using CreateFunction Method",1.0,"kdulani@andrew.cmu.edu","Test Description","None")
