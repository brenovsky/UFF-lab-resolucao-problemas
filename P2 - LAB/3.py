def excluir(L):
    nova = []
    for i in range(len(L)):
        if L[i] not in nova:
            nova.append(L[i])
    return nova

N = int(input())

resultado = []

for i in range(N):
    resultado.append(excluir(sorted(list(map(str, input().split())))))

for i in range(N):
    print(' '.join(map(str, resultado[i])))