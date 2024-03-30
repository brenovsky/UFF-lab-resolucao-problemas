N = int(input())
K = int(input())
tamanhos = list(map(int, input().split()))

maior = 0

for i in range(1, max(tamanhos)):
    fatias = 0
    for j in range(K):
        fatias += tamanhos[j] // i
    if fatias == N:
        maior = i

print(maior)

#código certo, porém o beecrowd dá time exceeded limit