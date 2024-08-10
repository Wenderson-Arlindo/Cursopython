velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado! A multa é de R${multa:.2f}")
else:
    print("Tenha um bom dia! Dirija com segurança!")