import random
n1 = str(input('Primeiro(a) aluno: '))

n2 = str(input('segundo(a) aluno: '))

n3 = str(input('terceiro(a) aluno: '))

n4 = str(input('quarto(a) aluno: '))

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista) 
print(f'O aluno escolhido foi {escolhido}')