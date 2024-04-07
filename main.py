from interface import JanelaAgendamentoJuridico

# Função para abrir o calendário


# def abrir_calendario():
#     calendario = Toplevel()
#     calendario.title("Selecionar Data")

#     data_selecionada = Calendar(calendario)
#     data_selecionada.pack()

#     # Função para fechar o calendário e atualizar o campo de entrada da data
#     def fechar_calendario():
#         data_alocacao_entry.delete(0, END)
#         data_alocacao_entry.insert(0, data_selecionada.get_date())
#         calendario.destroy()

#     botao_fechar = Button(calendario, text="Salvar data",
#                           command=fechar_calendario)
#     botao_fechar.pack()


# Cria a janela principal
janela = JanelaAgendamentoJuridico()

# Inicia o loop da janela
janela.mainloop()
