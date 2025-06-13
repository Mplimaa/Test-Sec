# Instalação do Bandit -- ferramenta de análise estática de segurança para código Python
# bandit -r seguranca.py
#demonstrar como usar o Bandit para analisar um código Python e detectar vulnerabilidades.
# pip install bandit

# Execução do Bandit:
# Após a instalação, você pode executar o bandit para analisar um arquivo ou diretório específico. Por exemplo:
# bandit -r path/to/your/code

# Exemplo de Script Python para Análise de Vulnerabilidades
# Aqui está um exemplo básico de script Python que você poderia analisar com o bandit:
import os

def insecure_deserialization(data):
    # Exemplo de código inseguro que pode ser suscetível a ataques
    return eval(data)

def list_files(directory):
    # Listar arquivos em um diretório, pode revelar informações sensíveis
    return os.listdir(directory)

# Exemplo de uso
data = "2 + 3"
print(insecure_deserialization(data))

directory = "C:\\Users\\Michele\\Documents"
print(list_files(directory))
