distancia=float(input("digite a distancia: "))
velocidade=float(input("digite a velocidade"))
tempo=distancia/velocidade
horas=int(tempo)
minutos=int((tempo - horas)*60)
segundos=int(((tempo - horas) * 60 - minutos)*60)
print(f"{horas}, hora(s) {minutos}, minutos {segundos}, segundos")