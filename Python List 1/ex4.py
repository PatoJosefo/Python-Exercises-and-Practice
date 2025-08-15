#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

salario = float(input('Digite o valor do salário: '))
aumento_percentual = float(input('Digite a porcentagem do aumento: '))

aumento = salario * (aumento_percentual / 100)
novo_salario = salario + aumento

print(f'O valor do aumento é: {aumento:.2f}')
print(f'O novo salário é: {novo_salario:.2f}')
