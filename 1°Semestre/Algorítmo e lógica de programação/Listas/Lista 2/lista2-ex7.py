metrosQuadrados = int(input("Quantos metros quadrados você irá pintar: "))

litros = metrosQuadrados / 3

numLata = litros / 18

if(numLata % 2) != 0:
    numLata = int(numLata) + 1

preco = numLata * 80

print(f'Você deverá comprar {numLata} latas de tintas, e isso custará R${preco: .2f}')
    
    
