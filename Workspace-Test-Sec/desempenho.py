import requests
import time

def test_website_speed(url, number_of_requests):
    total_time = 0

    for i in range(number_of_requests):
        start_time = time.time()  # Marca o início do pedido
        response = requests.get(url)
        end_time = time.time()    # Marca o fim do pedido

        request_time = end_time - start_time
        total_time += request_time

        print(f"Requisição {i + 1}: {request_time:.2f} segundos")

    average_time = total_time / number_of_requests
    print(f"\nTempo médio de resposta: {average_time:.2f} segundos")

# Exemplo de uso
url = "https://www.google.com.br"  # Substitua pela URL do site que deseja testar
number_of_requests = 50  # Número de requisições a serem feitas
test_website_speed(url, number_of_requests)


#pip install requests   executar  python desempenho.py
#Esse script mede o desempenho de carregamento de um site ao fazer 
# várias requisições HTTP e calcular o tempo médio de resposta.