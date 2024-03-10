num = int(input("Digite um número: "))

ant1 = 1
ant2 = 1

x = 0

#if num == 1 or num ==2:
#    print(f'O número que está na posição {num} é 1')

while x <= (num - 2):
    fibo = ant1 + ant2
    ant1 = ant2
    ant2 = fibo
    x = x + 1

print(f'O número 
