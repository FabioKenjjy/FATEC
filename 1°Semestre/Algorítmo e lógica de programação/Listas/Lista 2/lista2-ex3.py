peso = float(input("Qual o peso do peixe: "))

if peso > 50:
    pesoExcesso = peso - 50
    multa = pesoExcesso * 4
    print(f"O peso passou {pesoExcesso: .2f}Kg, então o valor da multa será de R${multa: .2f}")
else:
    print("O peso está dentro do limite, sem multa a pagar")
