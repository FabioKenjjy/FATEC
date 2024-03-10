nome = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")

while nome == senha:
    print("\n")
    print("Nome de usuário e senha não podem ser iguais!!! \n")
    nome = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    
print(f'Nome de usuário: {nome}')
print(f'Senha: {senha}')
