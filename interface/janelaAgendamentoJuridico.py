from tkinter import Tk, Label, Entry, Button, Toplevel, END
from tkcalendar import Calendar


class AgendamentoJuridico:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Agendamento Jurídico")

        # Labels
        self.nome_label = Label(self.janela, text="Nome:")
        self.sobrenome_label = Label(self.janela, text="Sobrenome:")
        self.cpf_label = Label(self.janela, text="CPF:")
        self.data_alocacao_label = Label(self.janela, text="Data de Alocação:")
        self.numero_whatsapp_label = Label(
            self.janela, text="Número WhatsApp:")

        # Entries
        self.nome_entry = Entry(self.janela)
        self.sobrenome_entry = Entry(self.janela)
        self.cpf_entry = Entry(self.janela)
        self.data_alocacao_entry = Entry(self.janela)
        self.numero_whatsapp_entry = Entry(self.janela)

        # Botões
        self.botao_calendario = Button(
            self.janela, text="Calendário", command=self.abrir_calendario)
        self.submit_button = Button(self.janela, text="Enviar")

        # Organizando os widgets
        self.nome_label.grid(row=0, column=0)
        self.nome_entry.grid(row=0, column=1)

        self.sobrenome_label.grid(row=1, column=0)
        self.sobrenome_entry.grid(row=1, column=1)

        self.cpf_label.grid(row=2, column=0)
        self.cpf_entry.grid(row=2, column=1)

        self.data_alocacao_label.grid(row=3, column=0)
        self.data_alocacao_entry.grid(row=3, column=1)
        self.botao_calendario.grid(row=3, column=2)

        self.numero_whatsapp_label.grid(row=4, column=0)
        self.numero_whatsapp_entry.grid(row=4, column=1)

        self.submit_button.grid(row=5, column=1)

        self.janela.mainloop()

    def abrir_calendario(self):
        # Função para abrir o calendário
        calendario = Toplevel()
        calendario.title("Selecionar Data")

        data_selecionada = Calendar(calendario)
        data_selecionada.pack()

        # Função para fechar o calendário e atualizar o campo de entrada da data
        def fechar_calendario():
            self.data_alocacao_entry .delete(0, END)
            self.data_alocacao_entry.insert(0, data_selecionada.get_date())
            calendario.destroy()

        botao_fechar = Button(calendario, text="Salvar data",
                              command=fechar_calendario)
        botao_fechar.pack()


if __name__ == "__main__":
    agendamento = AgendamentoJuridico()
