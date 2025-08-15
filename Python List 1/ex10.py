#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a dez mil.

resultado = 2 ** 10000
n_dig = len(str(resultado))

print(f'O número de dígitos em 2 elevado a 10.000 é: {n_dig}')
