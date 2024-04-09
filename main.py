from tkinter import Tk

from view import DadosJuridicos


janela = Tk()
janela.title("Agendamento Jurídico")

# Cria a janela principal
DadosJuridicos(master=janela)

janela.mainloop()
