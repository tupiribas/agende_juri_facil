import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class ServicoGoogleSheets:
    def __init__(self) -> None:
        # If modifying these scopes, delete the file token.json.
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

        # The ID and range of a sample spreadsheet.
        self.SAMPLE_SPREADSHEET_ID = "1VzpEt7gddPivhRWSUbmo1jX4SvxwMdU9hywLcnyrvNo"
        self.SAMPLE_RANGE_NAME = "Página1"

    def validacao_do_token(self):
        creds = None

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
        return creds

    def inserir_valor_na_linha(self, nome: str, sobrenome: str, cpf: str, data_nascimento: str, numero_telefone: str):
        creds = self.validacao_do_token()

        try:
            service = build("sheets", "v4", credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()

            ultima_linha = self.mostrar_ultima_linha()

            dados_novas_linhas = [
                [ultima_linha, nome, sobrenome,
                    cpf, data_nascimento, numero_telefone],
            ]

            # Adiciona as novas linhas
            result = sheet.values().append(
                spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                range="A:F",  # Insere em todas as colunas
                valueInputOption="USER_ENTERED",
                body={"values": dados_novas_linhas},
            ).execute()

            rows = result.get("values", [])
            print(f"{rows} rows retrieved")
            return result
        except HttpError as err:
            print(err)

    def mostrar_ultima_linha(self):
        creds = self.validacao_do_token()
        try:
            # Start no serviço
            service = build("sheets", "v4", credentials=creds)
            sheet = service.spreadsheets()

            # Obter os dados da tabela
            result = sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range="Página1!A:X").execute()

            # Retornando o tamanho da tabela somando com 1
            return len(result.get('values', []))
        except HttpError as err:
            print(err)