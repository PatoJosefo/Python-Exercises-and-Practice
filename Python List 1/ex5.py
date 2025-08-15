#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

preco = float(input('Digite o preço da mercadoria: '))
desconto_percentual = float(input('Digite o percentual de desconto: '))

desconto = preco * (desconto_percentual / 100)
preco_final = preco - desconto

print(f'O valor do desconto é: {desconto:.2f}')
print(f'O preço a pagar é: {preco_final:.2f}')