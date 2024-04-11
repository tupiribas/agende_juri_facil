import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class ConfigGoogleSheets:
    def __init__(self) -> None:
        # If modifying these scopes, delete the file token.json.
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

        # The ID and range of a sample spreadsheet.
        self.SAMPLE_SPREADSHEET_ID = "1VzpEt7gddPivhRWSUbmo1jX4SvxwMdU9hywLcnyrvNo"
        self.SAMPLE_RANGE_NAME = "Página1"

        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

    def mostrar_valores(self):
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file(
                "token.json", self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            service = build("sheets", "v4", credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = (
                sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                   range=self.SAMPLE_RANGE_NAME).execute()
            )

            rows = result.get("values", [])
            print(f"{rows} rows retrieved")
            return result
        except HttpError as err:
            print(err)


valor = ConfigGoogleSheets()
valor.mostrar_valores()
