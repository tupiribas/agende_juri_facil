from model.pessoa import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cpf: str, data_nascimento: str, numero_telefone: str) -> None:
        super().__init__(nome, sobrenome, data_nascimento, numero_telefone)
        self.cpf = cpf

    def __str__(self) -> str:
        return super().__str__()
