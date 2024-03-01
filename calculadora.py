
numero1 = float(input('Digite o primeiro numero:\n'))
calculo = float(input('Digite a funcao desejada para calculo : + ,- ,*,/'))
numero2 = float(input('Digite o segundo numero\n'))

soma = numero1+numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2
if calculo == '+' :
    print(soma)
if calculo =='-':
    print(subtracao)
if calculo == '*':
    print(multiplicacao)
if calculo == '/':
    print(divisao)