lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if ( (lado1 + lado2) > lado3 ) and  ( (lado3 + lado2) > lado1 ) and ( (lado1 + lado3) > lado2 ):
    if (lado1 == lado2) and (lado1 == lado3) and (lado2 == lado3):
        print("O triângulo é Equilátero")
    elif( (lado1 != lado2) and (lado1 == lado3) and (lado2 != lado3 ) ) or ( (lado1 != lado2) and (lado2 == lado3) and (lado1 != lado3) ) or ( (lado3 != lado2) and (lado1 == lado2) and (lado1 != lado3) ):
        print("O triângulo é isósseles")
    elif(lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
        print("O triângulo é escaleno")

else:
    print("Não é triângulo")
