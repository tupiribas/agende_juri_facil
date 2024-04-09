from tkinter import Tk, Frame, Label, Entry, Button, Toplevel, END
from tkcalendar import Calendar

from view.view_aba import AbaPadrao
from model.pessoa import PessoaFisica


class DadosJuridicos(AbaPadrao):
    # ALERTA! Melhorar a interface -> aumentar o espaçamento dos Entrys
    def __init__(self, master: Tk):
        # Inicialização do container
        super().__init__(master=master)

        self.aba_dados = self.criar_aba_padrao(titulo_da_aba="Dados Pessoais")

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

    def obter_dados_pessoa(self, nome, sobrenome, cpf, numero_telefone):
        pessoa = PessoaFisica(nome=self.nome_entry,
                              sobrenome=self.sobrenome_entry,
                              cpf=self.cpf_entry,
                              numero_telefone=self.numero_whatsapp_entry)

    def abrir_calendario(self):
        ''' Abre um calendário completo permitindo o
         usuário selecionar a data e salva na tela principal'''

        # Desabilitar o botão Calendário na tela principal
        self.botao_calendario.config(state="disabled")

        # Função para abrir o calendário
        calendario = Toplevel()
        calendario.title("Selecionar Data")
        data_selecionada = Calendar(calendario)
        data_selecionada.pack()

        def fechar_calendario():
            # Função para fechar o calendário e atualizar o campo de entrada da data
            self.data_alocacao_entry.delete(0, END)
            self.data_alocacao_entry.insert(0, data_selecionada.get_date())

            # Desabilitar o botão Calendário na tela principal
            self.botao_calendario.config(state="active")
            calendario.destroy()

        # Salvar informações
        botao_fechar = Button(calendario, text="Salvar data",
                              command=fechar_calendario)

        # Caso o usuário feche a janela do calendário, ele ativa o botão Calendário
        calendario.protocol("WM_DELETE_WINDOW", fechar_calendario)
        botao_fechar.pack()