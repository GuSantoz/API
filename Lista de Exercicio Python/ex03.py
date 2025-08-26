
nota1 = float(input('nota 1: '))
nota2 = float(input('nota2 : '))
    
media = (nota1 + nota2) / 2

if media >= 9 or media == 10: 
    print(f'Nota 1: {nota1} Nota 2: {nota2}, Media: {media}, Conceito: A, APROVADO!')
elif media >= 7.5 and media <= 9:  
    print(f'Nota 1: {nota1} Nota 2: {nota2}, Media: {media}, Conceito: B, APROVADO!')
elif media >= 6 and media <= 7.5: 
    print(f'Nota 1: {nota1} Nota 2: {nota2}, Media: {media}, Conceito: C, APROVADO!')
elif media >= 4 and media <= 6: 
    print(f'Nota 1: {nota1}/n Nota 2: {nota2}, Media: {media}, Conceito: D, REPROVADO!')
elif media >= 0 and media <= 4: 
    print(f'Nota 1: {nota1} Nota 2: {nota2}, Media: {media}, Conceito: E, REPROVADO!') 
    
    
    
    
    

    
    