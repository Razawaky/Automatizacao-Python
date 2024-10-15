# Inserir cada célula de cada linha em um campo do sistema
import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    # nome
    pyautogui.click(856,488,duration=0.1)
    pyautogui.write(linha[0].value)
    # produto
    pyautogui.click(844,524,duration=0.1)
    pyautogui.write(linha[1].value)
    # quantidade
    pyautogui.click(866,559,duration=0.1)
    pyautogui.write(str(linha[2].value))
    # categoria
    pyautogui.click(942,591,duration=0.1)
    pyautogui.write(linha[3].value)
    pyautogui.click(784,621,duration=0.1)
    pyautogui.click(786,577,duration=0.1)
    
    