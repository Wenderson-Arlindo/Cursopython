from random import shuffle

a1 = str(input("\n Digite o nome de um aluno: "))

a2 = str(input(" Digite o nome de mais um aluno: "))

a3 = str(input(" Digite o nome de outro aluno: "))

a4 = str(input(" Digite o nome do ultimo aluno: ")) 

list = [a1, a2, a3, a4]

shuffle(list)

print("\n A ordem de apresentação dos trabalhos será {}. \n".format(list))