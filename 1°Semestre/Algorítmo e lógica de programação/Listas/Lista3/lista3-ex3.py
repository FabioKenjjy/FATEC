A = 8
B = 20

anos = 0

while A <= B:
    A = A + ((A * 3)/100)
    B = B + ((B * 1.5)/100)
    anos = anos + 1

print(f'Levou {anos} anos para o país A igualar ou passar o país B')
