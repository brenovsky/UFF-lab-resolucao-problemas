def minu(x): #booleano para saber se a letra é maiúscula ou minuscula
    minuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if x in minuscula:
        return True
    return False

#definindo as letras (cada lista dentro de uma lista indica que as letras estão na mesma tecla)
minuscula = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
maiuscula = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
tel = [['2', '22', '222'], ['3', '33', '333'], ['4', '44', '444'], ['5', '55', '555'], ['6', '66', '666'], ['7', '77', '777', '7777'], ['8', '88', '888'], ['9', '99', '999', '9999']]

palavras = []
conversoes = []

N = int(input('digite quantas palavras quer escrever: '))

for x in range(N):

    conversao = []
    p = input('digite a palavra: ')
    palavras.append(p)

    for i in range(len(p) - 1): #navegar por cada letra

        if p[i] == ' ':
            conversao.append('0')

        elif minu(p[i]) == True:
            for k in range(len(minuscula)): #confere se p[i] é minúscula

                if p[i] in minuscula[k]:
                    tecla = k #encontrando a tecla de 'p[i]'
                    break
                    
            if p[i + 1] in minuscula[tecla]: #se a próxima letra estiver na mesma tecla... com *
                indice = minuscula[tecla].index(p[i])
                conversao.append(f'{tel[tecla][indice]}*')

    
            else:
                indice = minuscula[tecla].index(p[i])
                conversao.append(f'{tel[tecla][indice]}')

        else: #mesmos processos, mas agora com letra maiúscula
            for k in range(len(maiuscula)):

                if p[i] in maiuscula[k]:
                    tecla = k
                    break
            
            if minu(p[i + 1]) == True: #se a letra depois da maiúscula for minúscula...
                for k in range(len(minuscula)):

                    if p[i + 1] in minuscula[k]:
                        tecla2 = k
                        break

                if tecla == tecla2: #se estiverem na mesma tecla...
                    indice = maiuscula[tecla].index(p[i])
                    conversao.append(f'#{tel[tecla][indice]}*')
                
                else:
                    indice = maiuscula[tecla].index(p[i])
                    conversao.append(f'#{tel[tecla][indice]}')

            else:
                indice = maiuscula[tecla].index(p[i])
                conversao.append(f'#{tel[tecla][indice]}')

    #última letra
    if minu(p[-1]) == True:
        for k in range(len(minuscula)):

            if p[-1] in minuscula[k]:
                tecla = k
                break

        indice = minuscula[tecla].index(p[-1])
        conversao.append(f'{tel[tecla][indice]}')
        conversoes.append(conversao)

    else:
        for k in range(len(maiuscula)):

            if p[-1] in maiuscula[k]:
                tecla = k
                break

        indice = maiuscula[tecla].index(p[-1])
        conversao.append(f'#{tel[tecla][indice]}')
        conversoes.append(''.join(map(str, conversao)))

for i in range(N):
    print(f"{palavras[i]} = {''.join(map(str, conversoes[i]))}")