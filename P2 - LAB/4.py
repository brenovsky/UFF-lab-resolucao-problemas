while True:
    N = int(input())
    if N == 0:
        break

    matriz = [] 

    for i in range(N):
        linha = []

        for j in range(N):
            x = 2 ** (i + j)
            linha.append(x)

        matriz.append(linha)
    
    for i in range(N):
        print(matriz[i])
    print()

    #código errado
    #matriz = [[] * N] * N
    #for i in range(N):
        #for j in range(N):
            #matriz[i].append(2 ** (i + j))
    #for i in range(N):
        #print(matriz[i])
    #print()