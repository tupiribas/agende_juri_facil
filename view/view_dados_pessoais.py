from tkcalendar import Calendar
from tkinter import END, Button, Tk, Toplevel


from view.view_widgets import ViewLabelsPadrao, ViewEntryPadrao, ViewBotaoPadrao
from view.view_aba import ViewAbaPadrao


from controller.controle_agenda_juridico import ControleAgendaJuridico


class ViewDadosJuridicos(ViewAbaPadrao):
    # ALERTA! Melhorar a interface -> aumentar o espaçamento dos Entrys
    def __init__(self, master: Tk):
        # Inicialização do container
        super().__init__(master=master)

        self.aba_dados = self.criar_aba_padrao(titulo_da_aba="Dados Pessoais")

        self.label = ViewLabelsPadrao(self.aba_dados)
        self.entry = ViewEntryPadrao(self.aba_dados)
        self.botao = ViewBotaoPadrao(self.aba_dados,
                                     abrir_calendario_callback=self.abrir_calendario,
                                     salvar_informacoes_callback=self.__salvar_informacoes)

    def abrir_calendario(self):
        ''' Abre um calendário completo permitindo o
         usuário selecionar a data e salva na tela principal'''

        # Desabilitar o botão Calendário na tela principal
        self.botao.botao_calendario.config(state="disabled")

        # Função para abrir o calendário
        calendario = Toplevel()
        calendario.title("Selecionar Data")
        data_selecionada = Calendar(calendario, date_pattern='dd/mm/yyyy')
        data_selecionada.pack()

        def fechar_calendario():
            # Função para fechar o calendário e atualizar o campo de entrada da data
            self.entry.data_alocacao_entry.delete(0, END)
            self.entry.data_alocacao_entry.insert(
                0, data_selecionada.get_date())

            # Desabilitar o botão Calendário na tela principal
            self.botao.botao_calendario.config(state="active")
            calendario.destroy()

        # Salvar informações
        botao_fechar = Button(calendario, text="Salvar data",
                              command=fechar_calendario)

        # Caso o usuário feche a janela do calendário, ele ativa o botão Calendário
        calendario.protocol("WM_DELETE_WINDOW", fechar_calendario)
        botao_fechar.pack()

    def __salvar_informacoes(self):
        # Cadastrar Pessoas
        pessoa = ControleAgendaJuridico()
        pessoa.cadastrar_dados_pessoa_fisica(nome=self.entry.nome_entry.get(),
                                             sobrenome=self.entry.sobrenome_entry.get(),
                                             cpf=self.entry.cpf_entry.get(),
                                             data_nascimento=self.entry.data_nascimento_entry.get(),
                                             data_alocacao=self.entry.data_alocacao_entry.get(),
                                             numero_telefone=self.entry.numero_whatsapp_entry.get())
