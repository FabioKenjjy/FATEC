num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

menorNum = num1
maiorNum = num2

if menorNum > num2:
    menorNum = num2
    
if menorNum > num3:
    menorNum = num3
    
if maiorNum < num1:
    maiorNum = num1
    
if maiorNum < num3:
    maiorNum = num3

print(f"O menor número é {menorNum} e o maior número é {maiorNum}")

