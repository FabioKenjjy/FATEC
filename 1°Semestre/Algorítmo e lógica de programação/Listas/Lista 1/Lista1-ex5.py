mercadoria = float(input("Qual o valor da mercadoria: "))
porcentagem = int(input("Qual o percentual de desconto: "))

desconto = (mercadoria * porcentagem) / 100
novoPreco = mercadoria - desconto

print("Você terá R$", desconto, "de desconto, então o preço da mercadoria será R$", novoPreco)
