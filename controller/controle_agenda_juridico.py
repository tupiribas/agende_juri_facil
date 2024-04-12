from model.pessoa_fisica import PessoaFisica
from quickstart import ServicoGoogleSheets


class ControleAgendaJuridico:
    def obter_dados_pessoa_fisica(self, nome: str, sobrenome: str, cpf: str, data_nascimento: str, numero_telefone: str):
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
        if not cpf or not isinstance(cpf, str):
            raise ValueError("CPF inválido.")
        if not data_nascimento or not isinstance(data_nascimento, str):
            raise ValueError("Data de nascimento inválido.")
        if not numero_telefone or not isinstance(numero_telefone, str):
            raise ValueError("Número de telefone inválido.")

        # Criação do objeto PessoaFisica
        pessoafisica = PessoaFisica(
            nome=nome,
            sobrenome=sobrenome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            numero_telefone=numero_telefone,
        )

        sheets = ServicoGoogleSheets()
        sheets.validacao_do_token()
        sheets.inserir_valor_na_linha(nome=pessoafisica.nome,
                                      sobrenome=pessoafisica.sobrenome,
                                      cpf=pessoafisica.cpf,
                                      data_nascimento=pessoafisica.data_nascimento,
                                      numero_telefone=pessoafisica.numero_telefone)
