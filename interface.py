# Instalar o PySimpleGUI antes de rodar este arquivo:
# pip install PySimpleGUI 
# para mac/linux
# pip3 install PySimpleGUI

import PySimpleGUI as sg  # Importar a biblioteca PySimpleGUI

# Definir o tema da interface
sg.theme('Reddit')

# Lista de categorias de produtos
product_categories = [
    "Eletrônicos", "Móveis", "Roupas", "Brinquedos", "Comida", "Bebidas",
    "Cosméticos", "Livros", "Esportes", "Jardinagem"
]

# Configurar a estrutura da interface
layout = [
    [sg.Text('Cliente', size=(6, 0)), sg.Input(key='1', size=(20, 0))],  # Campo de entrada para cliente
    [sg.Text('Produto', size=(6, 0)), sg.Input(size=(20, 0), key='2')],  # Campo de entrada para produto
    [sg.Text('Quantidade'), sg.Input(key='3', size=(3, 0))],  # Campo de entrada para quantidade
    [sg.Text('Categoria do Produto'), sg.Combo(product_categories, key='4')],  # Combo box com opções de categorias
    [sg.Button('Salvar')]  # Botão para salvar os dados

]

# Criar a janela da interface
window = sg.Window('Cadastro de Produtos', layout)

# Loop principal da aplicação
while True:
    event, values = window.read()  # Ler eventos e valores da interface
    
    if event == sg.WIN_CLOSED:  # Verificar se a janela foi fechada
        break

    elif event == 'Salvar':  # Verificar se o botão Salvar foi clicado
        sg.popup('Produto Cadastrado')  # Exibir uma mensagem de confirmação
        window['1'].update('')  # Limpar o campo de cliente
        window['2'].update('')  # Limpar o campo de produto
        window['3'].update('')  # Limpar o campo de quantidade
        window['4'].update('')  # Limpar o combo box de categoria

