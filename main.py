from tkinter import Tk

from view.view_dados_pessoais import ViewDadosJuridicos


janela = Tk()
janela.title("Agendamento Jurídico")

# Cria a janela principal
ViewDadosJuridicos(master=janela)

janela.mainloop()
