num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maiorNum = num1

if maiorNum < num2:
    maiorNum = num2

if maiorNum < num3:
    maiorNum = num3

print(f"O maior número é {maiorNum}")
