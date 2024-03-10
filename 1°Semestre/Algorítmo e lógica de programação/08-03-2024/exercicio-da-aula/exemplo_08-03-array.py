#Faça um programa que leia uma data (dd-mm-aaaa)
#depois mostre o mês por extenso da data lida
#ex 08-03-2024 fica 08 de março de 2024
#dica:crie uma lista de meses por extenso
#leia a data e depois dê split('-') para separar
#dia mês e ano assim d, m, a = data.split('-')


meses = 'janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split()

d,m,a = input('data (dd-mm-aaaa): ').split('-')

print(d, 'de', meses[int(m) - 1], 'de', a)
