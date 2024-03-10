minutos = int(input("Quantos minutos você usou o telefone: "))

if minutos < 200:
    conta = minutos * 0.2

elif (minutos >= 200) and (minutos <= 400):
    conta = minutos * 0.18

elif minutos <= 800:
    conta = minutos * 0.15

else:
    conta = minutos * 0.08


print(f"Sua conta será de R$ {conta: .2f}")
