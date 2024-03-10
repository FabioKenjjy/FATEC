ganhoHora = float(input("Quantos você ganha por hora: "))

horasMes = int(input("Quantas horas você trabalha por mês: "))

salBruto = ganhoHora * horasMes

IR = (11 * salBruto) / 100
INSS = (8 * salBruto) / 100
sindicato = (5 * salBruto / 100)

descontos = IR + INSS + sindicato

salLiquido = salBruto - descontos

print(f"Salário Bruto = R${salBruto: .2f}")
print(f"INSS = R${INSS: .2f}")
print(f"Sindicato = R${sindicato: .2f}")
print(f"Salário Líquido = R${salLiquido: .2f}")

