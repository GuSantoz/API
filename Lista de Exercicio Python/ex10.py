import requests
x = input("Insira o cep do destino: ")
if len(x) == 8 and x.isdigit():
    response = requests.get(f"https://viacep.com.br/ws/{x}/json/?")
    if response.status_code == 200:
        response = response.json()
        bairro = response.get("bairro", "Não informado")
        regiao = response.get("regiao", "Não informado")
        cidade = response.get("localidade", "Não informado")
        print(f"Bairro: {bairro}, {regiao} de {cidade}")
    else:
         print("Erro na API")
else:
        print("Cep Inválido")