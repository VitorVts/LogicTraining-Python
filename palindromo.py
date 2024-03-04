
def palin():
    palavra = input('Informe uma palavra a ser invertida: ')
    reverse_str = palavra[::-1]
    if reverse_str == palavra :
        print('é palindromo')
    else :
        print('não é palindromo')
palin() 