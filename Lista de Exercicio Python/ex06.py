inicial = float(input("Salario inicial: "))
acressimo = 0.015
anoAtual = 2000
anoInicial = 1995
salario = inicial

for i in range(anoInicial + 1,anoAtual + 1):
    salario += salario * acressimo
    acressimo *= 2

print(f"Salario em {anoAtual} do funcionario é: {salario:.2f}")