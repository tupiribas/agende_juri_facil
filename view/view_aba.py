from tkinter import Frame


class ViewAbaPadrao(Frame):
    def __init__(self, master: Frame) -> None:
        """Cria e retorna uma aba personalizada."""
        super().__init__(master=master)

    def criar_aba_padrao(self, titulo_da_aba: str) -> Frame:
        from tkinter.ttk import Notebook
        # Cria o widget Notebook com base na janela master
        notebook = Notebook(self.master)
        notebook.pack()
        # Cria as abas
        aba = Frame(notebook)
        # Adiciona as abas ao Notebook
        notebook.add(aba, text=titulo_da_aba)

        return aba
