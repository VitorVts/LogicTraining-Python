def verifyPrimo():
    n = int(input("Informe um número para verificar se o mesmo é primo ou não"))
    primo = n > 1 and all(n % i != 0 for i in range(2,int(n**0.5)+1))
    if primo == True:
        print('É PRIMO MEU CHAPA')
    else :
        print('Não é primo')
verifyPrimo()

