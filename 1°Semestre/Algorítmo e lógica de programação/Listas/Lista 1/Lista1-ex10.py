cigarrosPorDia = int(input("Quantos cigarros você fuma por dia: "))
anosFumados = int(input("Quantos anos você fumou: "))

tempoPerdidoDia = cigarrosPorDia * 10
minPerdido = (tempoPerdidoDia * 365) * anosFumados
diasPerdidos = minPerdido / 1440

print(f"Você perdeu, {diasPerdidos:.2f} dias")
