distancia = int(input("Qual a distancia que você percorreu (em Km): "))
dias = int(input("Por quantos dias o carro foi alugado: "))

precoDia = dias * 60
precoDistancia = distancia * 0.15

precoTotal = precoDia + precoDistancia

print("O total a pagar será", precoTotal, "reais")

