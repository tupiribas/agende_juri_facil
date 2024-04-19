from tkinter import END, Button
from re import sub
from tkinter import Entry
from tkinter import Frame, Label


class ViewLabelsPadrao:
    def __init__(self, aba_padrao: Frame) -> None:
        # Labels
        self.nome_label = Label(aba_padrao, text="Nome:")
        self.sobrenome_label = Label(aba_padrao, text="Sobrenome:")
        self.cpf_label = Label(aba_padrao, text="CPF:")
        self.data_nascimento_label = Label(
            aba_padrao, text="Data de Nascimento:")
        self.data_alocacao_label = Label(
            aba_padrao, text="Data de Alocação:")
        self.numero_whatsapp_label = Label(
            aba_padrao, text="Número WhatsApp:")

        # Organizando os widgets
        self.nome_label.grid(row=0, column=0)
        self.sobrenome_label.grid(row=1, column=0)
        self.cpf_label.grid(row=2, column=0)
        self.data_nascimento_label.grid(row=3, column=0)
        self.data_alocacao_label.grid(row=4, column=0)
        self.numero_whatsapp_label.grid(row=5, column=0)


class ViewEntryPadrao:
    def __init__(self, aba_padrao: Frame) -> None:
        # Entries
        self.nome_entry = Entry(aba_padrao)
        self.sobrenome_entry = Entry(aba_padrao)
        self.cpf_entry = Entry(aba_padrao)
        self.data_nascimento_entry = Entry(aba_padrao)
        self.data_alocacao_entry = Entry(aba_padrao)
        self.numero_whatsapp_entry = Entry(aba_padrao)

        # Formatando o número de telefone enquanto o usuário digita
        self.numero_whatsapp_entry.bind('<KeyRelease>', self.formatar_numero)
        self.data_nascimento_entry.bind(
            '<FocusOut>', self.formatar_data_nascimento)
        self.data_alocacao_entry.bind(
            '<FocusOut>', self.formatar_data_alocacao)
        self.cpf_entry.bind('<FocusOut>', self.formatar_cpf)

        # Organizando os widgets
        self.nome_entry.grid(row=0, column=1)
        self.sobrenome_entry.grid(row=1, column=1)
        self.cpf_entry.grid(row=2, column=1)
        self.data_nascimento_entry.grid(row=3, column=1)
        self.data_alocacao_entry.grid(row=4, column=1)
        self.numero_whatsapp_entry.grid(row=5, column=1)

    def formatar_numero(self, event: None):
        # Obtém o número de telefone digitado pelo usuário
        numero = self.numero_whatsapp_entry.get()

        # Remove caracteres não numéricos do número
        numero_limpo = sub(r'\D', '', numero)

        # Verifica se o número tem 11 dígitos (formato brasileiro)
        if len(numero_limpo) == 11:
            numero_formatado = f'({numero_limpo[0:2]}) {
                numero_limpo[2:7]}-{numero_limpo[7:]}'
            self.numero_whatsapp_entry.delete(0, 'end')  # Limpa o campo
            self.numero_whatsapp_entry.insert(
                0, numero_formatado)  # Insere o número formatado

    def formatar_data_nascimento(self, event: None):
        # Obtém a data digitada pelo usuário
        data = self.data_nascimento_entry.get()

        # Remove caracteres não numéricos da data
        data_limpa = ''.join(filter(str.isdigit, data))

        # Adiciona as barras separadoras
        if len(data_limpa) >= 3:
            data_formatada = f"{
                data_limpa[:2]}/{data_limpa[2:4]}/{data_limpa[4:8]}"
            self.data_nascimento_entry.delete(0, 'end')  # Limpa o campo
            self.data_nascimento_entry.insert(
                0, data_formatada)  # Insere a data formatada

    def formatar_data_alocacao(self, event: None):
        # Obtém a data digitada pelo usuário
        data = self.data_alocacao_entry.get()

        # Remove caracteres não numéricos da data
        data_limpa = ''.join(filter(str.isdigit, data))

        # Adiciona as barras separadoras
        if len(data_limpa) >= 3:
            data_formatada = f"{
                data_limpa[:2]}/{data_limpa[2:4]}/{data_limpa[4:8]}"
            self.data_alocacao_entry.delete(0, 'end')  # Limpa o campo
            self.data_alocacao_entry.insert(
                0, data_formatada)  # Insere a data formatada

    def formatar_cpf(self, event: None):
        # Obtém o CPF digitado pelo usuário
        cpf = self.cpf_entry.get()

        # Remove caracteres não numéricos do CPF
        cpf_limpo = ''.join(filter(str.isdigit, cpf))

        # Verifica se o CPF tem 11 dígitos
        if len(cpf_limpo) == 11:
            # Formata o CPF com pontos e traço
            cpf_formatado = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{
                cpf_limpo[6:9]}-{cpf_limpo[9:]}"

            # Atualiza o campo de entrada do CPF com o CPF formatado
            self.cpf_entry.delete(0, 'end')
            self.cpf_entry.insert(0, cpf_formatado)
        else:
            # Se o CPF não tiver 11 dígitos, limpa o campo
            self.cpf_entry.delete(0, 'end')


class ViewBotaoPadrao:
    def __init__(self, aba_padrao: Frame, salvar_informacoes_callback, abrir_calendario_callback) -> None:
        self.aba_padrao = aba_padrao

        # Botões
        self.botao_calendario = Button(
            aba_padrao, text="Calendário", command=abrir_calendario_callback)
        self.botao_calendario.grid(row=4, column=2)

        self.submit_button = Button(
            aba_padrao, text="Enviar", command=salvar_informacoes_callback)
        self.submit_button.grid(row=6, column=1)
