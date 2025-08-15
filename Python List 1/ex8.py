#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km_percorridos = float(input('Digite a quantidade de km percorridos: '))
dias_alugados = int(input('Digite a quantidade de dias alugados: '))

preco_por_dia = 60.00
preco_por_km = 0.15

preco_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)

print(f'O preço total a pagar é: R$ {preco_total:.2f}')