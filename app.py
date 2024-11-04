# Inserir cada célula de cada linha em um campo do sistema

import openpyxl  # Biblioteca para ler e escrever arquivos Excel
import pyautogui  # Biblioteca para automação de interface gráfica

# Carregar o livro Excel e acessar a planilha 'vendas'
workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

# Iterar sobre todas as linhas da planilha, começando na segunda linha (índice 2)
for linha in vendas_sheet.iter_rows(min_row=2):
    # Nome do cliente
    pyautogui.click(856, 488, duration=0.1)  # Clicar no campo de texto
    pyautogui.write(linha[0].value)  # Digitar o valor da célula A
    
    # Nome do produto
    pyautogui.click(844, 524, duration=0.1)  # Clicar no campo de texto
    pyautogui.write(linha[1].value)  # Digitar o valor da célula B
    
    # Quantidade
    pyautogui.click(866, 559, duration=0.1)  # Clicar no campo de texto
    pyautogui.write(str(linha[2].value))  # Digitar o valor da célula C como string
    
    # Categoria do produto
    pyautogui.click(942, 591, duration=0.1)  # Clicar no campo de texto
    pyautogui.write(linha[3].value)  # Digitar o valor da célula D
    
    # Salvar os dados
    pyautogui.click(784, 621, duration=0.1)  # Clicar no botão salvar
    pyautogui.click(786, 577, duration=0.1)  # Confirmar ação de salvar
