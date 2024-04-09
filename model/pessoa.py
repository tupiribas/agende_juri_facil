class PessoaFisica:
    def __init__(self, nome, sobrenome, cpf, numero_telefone) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.numero_telefone = numero_telefone

    def __str__(self) -> str:
        return f'{self.nome}, {self.sobrenome}, {self.cpf}, {self.numero_telefone}.'