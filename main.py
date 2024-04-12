from tkinter import Tk

from quickstart import ServicoGoogleSheets
from view.view_dados_pessoais import ViewDadosJuridicos

# Start na API do google
sheets = ServicoGoogleSheets()
sheets.validacao_do_token()

janela = Tk()
janela.title("Agendamento Jurídico")

# Cria a janela principal
ViewDadosJuridicos(master=janela)

janela.mainloop()
