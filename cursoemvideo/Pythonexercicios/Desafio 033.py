n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
n3 = int(input('Digite o Terçeiro Número: '))
# verificando maior
if n1 >= n2 and n1 >= n3:
    beeg = n1
if n2 >= n3 and n2 >= n1:
    beeg = n2
if n3 >= n2 and n3 >= n1:
    beeg = n3
# verificando menor
if n1 <= n2 and n1 <= n3:
    smol = n1
if n2 <= n1 and n2 <= n3:
    smol = n2
if n3 <= n1 and n2 <= n2:
    smol = n3
print(f'o maior numero é {beeg}')
print(f'O menor número é {smol}')
