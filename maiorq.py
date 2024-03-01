numero1 = float(input('Digite um numero'))
numero2 = float(input('Digite um numero'))
numero3 = float(input('Digite um numero'))

maior = numero1
if(numero2>maior):
    maior = numero2
if(numero3>maior):
    maior= numero3
print(f'O Maior numero é ,{maior}')