tipo = input("Informe o tipo do combustivel: ")
qtd = float(input("Informe a quantidade(L): "))
gasolina = 2.50
alcool = 1.90

if tipo == "A" or tipo == "a":
    if qtd > 20:
        total = qtd * (alcool - (alcool*0.05))
    else:
        total = qtd * (alcool - (alcool*0.03))
elif tipo == "G" or tipo == "g":
    if qtd > 20:
        total = qtd * (gasolina - (gasolina*0.06))
    else:
        total = qtd * (gasolina - (gasolina*0.04))

print(f'{total:.2f}')
