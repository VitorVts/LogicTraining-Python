#minha solucao 

palavra = input('digite a palavra ')
nvogal=0
for i in palavra:
    if i == 'a':
        nvogal+=1
    elif i == 'e':
        nvogal+=1
    elif i == 'i':
        nvogal+=1
    elif i == 'o':
        nvogal+=1
    elif i == 'u':
        nvogal+=1
print(f'A palavra {palavra} inserida tem {nvogal} vogais')

# solucao do chat 

# palavra = input('Digite a palavra: ')
# nvogal = 0

# for letra in palavra:
#     if letra.lower() in 'aeiou':
#         nvogal += 1

# print(f'A palavra {palavra} inserida tem {nvogal} vogais.')


