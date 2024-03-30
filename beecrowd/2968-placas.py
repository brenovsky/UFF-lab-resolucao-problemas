V, N = map(int, input().split())
lista = []
ultima = 0
for i in range(10, 100, 10):
    for placa in range(ultima, V * N):
        if ((placa * 100) // (V * N)) >= i:
            lista.append(placa)
            ultima = placa
            break
print(' '.join(map(str, lista)))