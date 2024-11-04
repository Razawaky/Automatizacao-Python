# Instalar o PySimpleGUI antes de rodar este arquivo:
# pip install PySimpleGUI 
# para mac/linux
# pip3 install PySimpleGUI

import PySimpleGUI as sg  # Importar a biblioteca PySimpleGUI

from cryptography.fernet import Fernet 

# Definir o tema da interface
sg.theme('Reddit')

# Função para gerar chave de criptografia
def generate_key():
    return Fernet(base64.urlsafe_b64encode(os.urandom(32)))

# Gerar chave de criptografia
key = generate_key()
with open("encryption_key.txt", "wb") as key_file:
    key_file.write(key)

# Decodificar a chave armazenada
with open("encryption_key.txt", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Função para criptografar dados
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

# Função para descriptografar dados
def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()

# Função para validar credenciais
def validate_credentials(username, password):
    # Substitua isso pela sua lógica real de autenticação
    return username == "admin" and password == "password123"

# Função para iniciar sessão
def start_session():
    layout = [
        [sg.Text("Username:")],
        [sg.Input(key="-USERNAME-", size=(20, 1))],
        [sg.Text("Password:")],
        [sg.Input(key="-PASSWORD-", size=(20, 1), password_char="*")],
        [sg.Button("Login"), sg.Button("Cancel")]
    ]
    window = sg.Window("Login", layout)
    
    while True:
        event, values = window.read()
        if event == "Login":
            username = values["-USERNAME-"]
            password = values["-PASSWORD-"]
            
            if validate_credentials(username, password):
                sg.popup("Login successful!")
                return username
            else:
                sg.popup("Invalid credentials.")
        elif event == sg.WINDOW_CLOSED or event == "Cancel":
            return None
    
    window.close()

# Função para proteger dados sensíveis
def protect_sensitive_data(data):
    encrypted_data = encrypt_data(data)
    return encrypted_data

# Função para recuperar dados sensíveis
def get_sensitive_data(encrypted_data):
    decrypted_data = decrypt_data(encrypted_data)
    return decrypted_data

# Função para criar interface
def create_interface(username):

# Lista de categorias de produtos
product_categories = [
    "Eletrônicos", "Móveis", "Roupas", "Brinquedos", "Comida", "Bebidas",
    "Cosméticos", "Livros", "Esportes", "Jardinagem"
]

# Configurar a estrutura da interface
    # ... (resto do código da interface permanece o mesmo)

#     except ValueError as ve:
#     sg.popup_error(f"Erro: {str(ve)}")
#     except Exception as e:
#     sg.popup_error(f"Um erro inesperado ocorreu: {str(e)}")

# Função para limpar dados sensíveis
def clear_sensitive_data():

# Função para salvar dados sensíveis
def save_sensitive_data(data):

# Função para recuperar dados sensíveis
def load_sensitive_data():

# Função para excluir dados sensíveis
def delete_sensitive_data():

# Função para criar interface
def criar_interface():
    username = start_session()
    if not username:
        return

    layout = [
        [sg.Text('Cliente', size=(6, 0)), sg.Input(key='1', size=(20, 0))],
        [sg.Text('Produto', size=(6, 0)), sg.Input(size=(20, 0), key='2')],
        [sg.Text('Quantidade'), sg.Input(key='3', size=(3, 0))],
        [sg.Text('Categoria do Produto'), sg.Combo(product_categories, key='4')],
        [sg.Button('Salvar'), sg.Button('Logout')]
    ]
    
    window = sg.Window('Cadastro de Produtos', layout)
    
    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == 'Logout':
            break
        
        elif event == 'Salvar':
            # Criptografar dados sensíveis antes de salvar
            protected_data = protect_sensitive_data(f"{values['1']},{values['2']},{values['3']},{values['4']}")
            # Aqui você pode salvar os dados protegidos em um arquivo ou banco de dados
            
            sg.popup('Produto Cadastrado')
            clear_fields(window)
    
    window.close()

# Função para limpar campos da interface
def clear_fields(window):
    for key in window.keys():
        if key.startswith('-'):
            window[key].update('')
    window['1'].update('')
    window['2'].update('')
    window['3'].update('')
    window['4'].update('')

# Função para criar janela principal
def criar_janela_principal():
    criar_interface()

# Função para iniciar o programa
def main():
    criar_janela_principal()

if __name__ == "__main__":
    main()
            
#     except ImportError:
#     print("A biblioteca PySimpleGUI não está instalada. Por favor, instale-a usando 'pip install PySimpleGUI'")
#     except Exception as e:
#     print(f"Um erro inesperado ocorreu: {str(e)}")

# if __name__ == "__main__":
#     criar_interface()
