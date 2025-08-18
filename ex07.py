qtdV = 1 
nums = []
soma= 0
num = int(input('dig um num: '))
acima_media = 0
while num != -1:
    soma += num 
    nums.append(num)
    num = int(input('dig um num: '))
    media = soma / qtdV
    qtdV += 1
    
for x in nums:
    if x > 10:
        acima_media += 1
        

print(f'Valores informados na ordem: {nums}')
print(f'Valores informados na ordem inversa: {list(reversed(nums))}')
print(f'Quantidade de valores informados: {qtdV}')
print(f'Soma dos valores informados: {soma}')
print(f'Média dos valores informados: {media:.2f}')
print(f'Valores acima da média: {acima_media}')