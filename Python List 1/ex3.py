#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos

d = int(input('Digite a quantidade de dias: '))
h = int(input('Digite a quantidade de horas: '))
m = int(input('Digite a quantidade de minutos: '))
s = int(input('Digite a quantidade de segundos: '))

ts = (d * 86400) + (h * 3600) + (m * 60) + s

print(f'O total de segundos é {ts}')

