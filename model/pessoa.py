class Pessoa:
    def __init__(self, nome, sobrenome, data_nascimento, numero_telefone) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.numero_telefone = numero_telefone
        self.data_nascimento = data_nascimento

    def __str__(self) -> str:
        return f'{self.nome}, {self.sobrenome}, {self.data_nascimento}, {self.numero_telefone}.'
