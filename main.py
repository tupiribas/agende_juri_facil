from tkinter import Tk

from quickstart import ServicoGoogleSheets
from view.view_dados_pessoais import ViewDadosJuridicos

# Start na API do Google
sheets = ServicoGoogleSheets()
sheets.validacao_do_token()

# Start - Janela do Tkinter
janela = Tk()
janela.title("Agendamento Jurídico")
# Cria a janela principal
ViewDadosJuridicos(master=janela)

janela.mainloop()
