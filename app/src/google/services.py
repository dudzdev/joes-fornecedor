import gspread
from gspread import Worksheet
from oauth2client.service_account import ServiceAccountCredentials

from src import config


class GoogleSheetsService:

    def __init__(self):
        credentials_path = config.CREDENTIALS_GOOGLE_LOCAL_PATH+config.CREDENTIALS_GOOGLE_FILE_NAME
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            filename=credentials_path,
            scopes=[
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive",
            ]
        )
        self.__client = gspread.authorize(creds)

    def get_worksheet(self, folder_id: str, title: str) -> Worksheet:
        workbook = self.__client.open(title=title, folder_id=folder_id)
        worksheet = workbook.get_worksheet(0)
        return worksheet

    def append_row(self, worksheet: Worksheet, values: list) -> bool:
        worksheet.append_row(values)
        return True
