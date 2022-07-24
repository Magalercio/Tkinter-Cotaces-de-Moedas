import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

lista_moedas = ['USD', 'EUR']


def pegar_cotacao():
    pass


janela = tk.Tk()

janela.title('Ferramenta de cotação de moedas')

label_cotacaomoeda = tk.Label(text='Cotação de 1 Moeda Específica', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionarmoeda = tk.Label(text='Selecionar a moeda que deseja consultar:')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionarmoeda = tk.Label(text='Selecione o dia que deseja pegar a cotação:')
label_selecionarmoeda.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_pegarcotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# Cotaçao de Várias moedas
label_cotacaovariasmoeda = tk.Label(text='Cotação de Múltiplas Moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoeda.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

janela.mainloop()
