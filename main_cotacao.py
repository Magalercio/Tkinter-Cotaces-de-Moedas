import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

lista_moedas = ['USD', 'EUR']


def pegar_cotacao():
    pass


def selecionar_arquivo():
    pass


def atualizar_cotacoes():
    pass


janela = tk.Tk()

janela.title('Ferramenta de cotação de moedas')

label_cotacaomoeda = tk.Label(text='Cotação de 1 Moeda Específica', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionarmoeda = tk.Label(text='Selecionar a moeda que deseja consultar:', anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionardia = tk.Label(text='Selecione o dia que deseja pegar a cotação:', anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_pegarcotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# Cotaçao de Várias moedas
label_cotacaovariasmoeda = tk.Label(text='Cotação de Múltiplas Moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoeda.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionararquivo = tk.Label(text='Selecione um arquivo em Excel com as Moedas na Coluna A:')
label_selecionararquivo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_selecionararquivo = tk.Button(text='Clique para Selecionar', command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

label_arquivoselecionado = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

label_datainicial = tk.Label(text='Data Inicial', anchor='e')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='nswe')
label_datafinal = tk.Label(text='Data Final', anchor='e')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='nswe')

calendario_datainicial = DateEntry(year=2022, locale='pt_br')
calendario_datafinal = DateEntry(year=2022, locale='pt_br')
calendario_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

botao_atualizarcotacoes = tk.Button(text='Atualizar Cotações', command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')

label_atualisarcotacoes= tk.Label(text='')
label_atualisarcotacoes.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar Programa', command=janela.quit, fg='red', bg='ivory3')
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
