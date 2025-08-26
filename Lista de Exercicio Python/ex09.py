#Poderiamos criar um dicionario com todas as traduções das #moedas, porem escolhemos utilizar uma API que nos fornece #essa resposta

import requests
x = input("Digite a sigla da moeda desejada: ").upper()

response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{x}")
responseNome = requests.get(f"https://economia.awesomeapi.com.br/json/last/{x}-BRL")
responseNome = responseNome.json()
response = response.json()
taxa = response["rates"]["BRL"]
nome = responseNome[f"{x}BRL"]["name"]
print(f"O Real vale {taxa} {nome}”, onde {taxa} é o valor da cotação.")