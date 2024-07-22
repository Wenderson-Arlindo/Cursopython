import math 
an = int(input("Digite o ângulo que você deseja: ")) 
ra = math.radians(an) 
print("O ângulo de {} tem o COSSENO de {:.2f}".format(an, math.cos(ra))) 
print("O angulo de {} tem o SENO de {:.2f}".format(an, math.sin(ra))) 
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(an, math.tan(ra)))