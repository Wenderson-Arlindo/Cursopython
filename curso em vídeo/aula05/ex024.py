frase = str(input('Digite qualquer frase: ')). upper().strip()

print(f'A letra "A" aparece em sua frase (frase.count("A")} vezes.')

print(f'A letra "A" aparece pela primeira vez em sua frase em {frase.find("A") + 1}')

print(f'A letra "A" aparece em sua frase pela última vez em {frase.rfind("A") + 1}')