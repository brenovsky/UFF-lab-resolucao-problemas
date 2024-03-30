J, R = map(int, input().split())
a = list(map(int, input().split()))
pontos = []
for i in range(J):
    soma = 0
    for j in range(i, J * R, J):
        soma += a[j]
    pontos.append(soma)
for i in range(len(pontos) - 1, -1, -1):
    if pontos[i] == max(pontos):
        print(i + 1)
        break