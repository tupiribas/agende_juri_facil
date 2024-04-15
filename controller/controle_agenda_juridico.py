from re import match
from model.agendamento import Agendamento
from model.pessoa_fisica import PessoaFisica
from model.telefone import NumeroTelefone
from quickstart import ServicoGoogleSheets


class ControleAgendaJuridico:
    def cadastrar_dados_pessoa_fisica(self, nome: str, sobrenome: str, cpf: str, data_nascimento: str, data_alocacao: str, numero_telefone: str):
        """
        Obtém os dados da pessoa e cria um objeto PessoaFisica.

        Args:
            nome (str): Nome da pessoa.
            sobrenome (str): Sobrenome da pessoa.
            cpf (str): CPF da pessoa.
            numero_telefone (str): Número de telefone da pessoa.

        Returns:
            PessoaFisica: Objeto PessoaFisica com os dados da pessoa.
        """
        # Validação de dados
        if not nome or not isinstance(nome, str):
            raise ValueError("Nome inválido.")
        if not sobrenome or not isinstance(sobrenome, str):
            raise ValueError("Sobrenome inválido.")
        # Ponto de melhoria: Verificar o cpf da pessoa é valido
        if not cpf:
            raise ValueError("Preencha o CPF.")
        if not match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            raise ValueError("Formato do CPF ta errado.")
        if not data_nascimento:
            raise ValueError("Preencha uma data de nascimento.")
        if not match(r'\d{2}/\d{2}/\d{4}', data_nascimento):
            raise ValueError("Formato da data de nasciemento ta errado.")
        if not data_alocacao:
            raise ValueError("Preencha uma data de alocação.")
        if not match(r'\d{2}/\d{2}/\d{4}', data_alocacao):
            raise ValueError("Formato da data de alocação ta errado.")
        if not numero_telefone:
            raise ValueError("Preencha o numero de telefone.")
        if not bool(match(r'^\(\d{2}\) \d{5}-\d{4}$', numero_telefone)):
            raise ValueError("Formato de numero de telefone ta errado.")

            # Criação do objeto PessoaFisica
        pessoafisica = PessoaFisica(
            nome=nome,
            sobrenome=sobrenome,
            cpf=cpf,

            data_nascimento=data_nascimento
        )
        numero_pessoa = NumeroTelefone(numero=numero_telefone)
        agendamento_pessoa = Agendamento(data=data_alocacao)

        # Inserir os valores na planilha do Google
        sheets = ServicoGoogleSheets()
        sheets.validacao_do_token()
        sheets.inserir_valor_na_linha(nome=pessoafisica.nome,
                                      sobrenome=pessoafisica.sobrenome,
                                      cpf=pessoafisica.cpf,
                                      data_alocacao=agendamento_pessoa.data,
                                      data_nascimento=pessoafisica.data_nascimento,
                                      numero_telefone=numero_pessoa.numero)
