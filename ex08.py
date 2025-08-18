import requests
x = input("Inisira o nome (em ingles) do país desejado: ")
x = x.lower()
response = requests.get(f"https://restcountries.com/v3.1/name/{x}")

if response.ok:
    retorno = response.json()
    pais = retorno[0]
    nome_comum = pais["translations"]["por"]["common"]
    linguagem = list(pais["languages"].values())[0]
    regiao = pais["region"]
    subRegiao = pais["subregion"]
    capital = pais["capital"][0]
    siglaMoeda = list(pais["currencies"])[0]
    moeda = list(pais["currencies"])[0][0]
    simboloMoeda = list(pais["currencies"])[0][1]
        
    print(f'Nome do País: {nome_comum.upper()}')
    print(f'Linguagem oficial: {linguagem.upper()}')
    print(f'Região: {regiao}')
    print(f'Sub Região: {subRegiao}, Capital: {capital}')
    print(f'Sigla da moeda: {siglaMoeda}')
    print(f'Moeda Oficial: {moeda} "{simboloMoeda}"')
    try:
        fronteira = list(pais["borders"])
    except:
        print("O país não faz fronteira com nenhum outro")
    else:
        print(f'Os paises que fazem fronteira são: {fronteira}')
else:
    print("Erro na api")
