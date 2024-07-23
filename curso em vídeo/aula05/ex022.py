nome = input(("Digite seu nome completo: ")).strip()

print(nome.upper())

print(nome.lower())

nome_split = nome.split()

nome_replace = nome.replace(" ","")

print(len(nome_replace))

print(len(nome_split[0]))