n = int(input("Digite o valor total: "))
notas = [100, 50, 10, 5, 1]
valor = n
if 10 <= valor <= 600:
    for nota in notas:
        qtd = valor // nota
        valor -= qtd * nota
        print(f'{qtd} nota(s) de R$ {nota},00')
else:
    print("O valor tem que estar entre 10 e 600 reais")