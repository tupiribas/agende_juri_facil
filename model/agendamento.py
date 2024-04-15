class Agendamento:
    def __init__(self, data):
        self.data = data
        self.descricao = None

    def __str__(self):
        return f"Agendamento: {self.data.strftime('%d/%m/%Y')} - {self.descricao}"
