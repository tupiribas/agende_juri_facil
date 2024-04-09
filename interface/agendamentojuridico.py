from tkinter import Tk, Label, Entry, Button, Toplevel, END
from tkinter.ttk import Notebook, Frame
from tkcalendar import Calendar


class AgendamentoJuridico:
    # Melhorar a interface -> aumentar o espaçamento dos Entrys
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Agendamento Jurídico")

        # Cria o widget Notebook
        self.notebook = Notebook(self.janela)
        self.notebook.pack()
        # Cria as abas
        self.aba_dados = Frame(self.notebook)
        # Adiciona as abas ao Notebook
        self.notebook.add(self.aba_dados, text="Dados Pessoais")

        # Labels
        self.nome_label = Label(self.aba_dados, text="Nome:")
        self.sobrenome_label = Label(self.aba_dados, text="Sobrenome:")
        self.cpf_label = Label(self.aba_dados, text="CPF:")
        self.data_alocacao_label = Label(
            self.aba_dados, text="Data de Alocação:")
        self.numero_whatsapp_label = Label(
            self.aba_dados, text="Número WhatsApp:")

        # Entries
        self.nome_entry = Entry(self.aba_dados)
        self.sobrenome_entry = Entry(self.aba_dados)
        self.cpf_entry = Entry(self.aba_dados)
        self.data_alocacao_entry = Entry(self.aba_dados)
        self.numero_whatsapp_entry = Entry(self.aba_dados)

        # Botões
        self.botao_calendario = Button(
            self.aba_dados, text="Calendário", command=self.abrir_calendario)
        self.submit_button = Button(self.aba_dados, text="Enviar")

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
        # Desabilitar o botão Calendário na tela principal
        self.botao_calendario.config(state="disabled")

        # Função para abrir o calendário
        calendario = Toplevel()
        calendario.title("Selecionar Data")
        data_selecionada = Calendar(calendario)
        data_selecionada.pack()

        # Função para fechar o calendário e atualizar o campo de entrada da data
        def fechar_calendario():
            self.data_alocacao_entry.delete(0, END)
            self.data_alocacao_entry.insert(0, data_selecionada.get_date())

            # Desabilitar o botão Calendário na tela principal, quando salvar ou fechar
            self.botao_calendario.config(state="active")
            calendario.destroy()

        botao_fechar = Button(calendario, text="Salvar data",
                              command=fechar_calendario)
        botao_fechar.pack()
