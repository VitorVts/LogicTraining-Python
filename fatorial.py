


def calc_fatorial(numero):
    if numero < 0:
        return "Nãoé possivel calcular o fatorial de um número negativo"
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2,numero+ 1):
            fatorial*= i
        return fatorial

numero = int(input("Digitite o numero para calcular o fatorial "))
resultado = calc_fatorial(numero)
print(resultado)