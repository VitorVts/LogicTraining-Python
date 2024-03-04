

    
def calcular_imc(altura,peso):
    
    n=10000
    imc = n*(peso/(altura*altura))
    imc_format= "{:.0f}".format(imc)
    print(imc_format)
    if imc < 24.9 :
        print('Abaixo do normal')
    elif imc <29.9 :
        print('Sobrepeso')
    elif imc <34.9:
        print("Obesidade grau 1") 
    elif imc <39.9:
        print("Obesidade Grau 2")
    else :
        print("Obesidade Grau 3 ")


print('\n Bem vindo(a) a calculadora de imc informe as informações solicitadas a baixo...: \n\n')
altura = float(input('Digite sua altiura..:'))
peso = float(input('Digite Seu peso'))


calcular_imc(altura,peso)