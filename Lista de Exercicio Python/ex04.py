certas = ["a", "b", "c", "d", "a", "b", "c", "d", "a", "b"]
respostas = []
for i in range(10):
    p = input(f"Resposta da questão {i+1}: ")
    respostas.append(p)
    
x = 0
for resposta in respostas:
    if resposta == certas[x]:
        print(f'Resposta questão {x+1} etá correta')
    else:
        print(f'Resposta questão {x+1} etá incorreta')
    x+=1
