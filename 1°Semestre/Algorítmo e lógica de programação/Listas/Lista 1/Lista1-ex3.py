dias = int(input("Número de dias: "))
horas = int(input("Número de horas: "))
minutos = int(input("Número de minutos: "))
segundos = int(input("Número de segundos: "))

minSeg = minutos * 60
horaSeg = horas * 3600
diaSeg = dias * 86400

totalSeg = (segundos + minSeg + horaSeg + diaSeg)

print("O total de segundos é", totalSeg)
