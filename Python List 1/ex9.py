#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros_por_dia = int(input("Quantos cigarros você fuma por dia: "))
anos_fumando = int(input("Há quantos anos você fuma: "))

total_cigarros = cigarros_por_dia * 365 * anos_fumando
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / (60 * 24)

print(f"Você perdeu aproximadamente {dias_perdidos:.0f} dias de vida.")

