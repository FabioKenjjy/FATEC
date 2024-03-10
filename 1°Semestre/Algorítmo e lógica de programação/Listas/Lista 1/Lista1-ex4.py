salario = float(input("Digite seu salário: "))
porcentagem = int(input("Digite a porcentagem de aumento: "))

aumento = (salario * porcentagem) / 100
novoSal = salario + aumento

print("Você irá ganhar R$", aumento, "A mais, seu novo salário será de R$", novoSal)

