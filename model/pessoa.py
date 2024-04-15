class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_nascimento: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def __str__(self) -> str:
        return f'{self.nome}, {self.sobrenome}, {self.data_nascimento}.'
