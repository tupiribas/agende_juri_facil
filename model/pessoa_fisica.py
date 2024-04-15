from model.pessoa import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cpf: str, data_nascimento: str) -> None:
        super().__init__(nome, sobrenome, data_nascimento)
        self.cpf = cpf

    def __str__(self) -> str:
        return super().__str__()
