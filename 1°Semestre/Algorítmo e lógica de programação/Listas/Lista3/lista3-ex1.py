nota = int(input("Digite uma nota de 0 à 10: "))

while nota < 0 or nota > 10:
    print("digite um valor válido!!!")
    nota = int(input("Digite uma nota de 0 à 10: "))

print(f'O valor digitado foi {nota}')
