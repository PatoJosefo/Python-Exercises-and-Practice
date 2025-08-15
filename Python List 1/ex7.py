#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32 8) Faça agora o contrário, de Fahrenheit para Celsius.

celcius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (9 * celcius / 5) + 32

print(f'{celcius} graus Celsius é igual a {fahrenheit} graus Fahrenheit')