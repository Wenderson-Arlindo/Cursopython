import random

numero = random.randint(0, 5)
palpite = int(input("Em que número eu pensei? (entre 0 e 5): "))
if palpite == numero:
    print("Parabéns! Você acertou!")
else:
    print(f"Que pena! Eu pensei no número {numero}.")