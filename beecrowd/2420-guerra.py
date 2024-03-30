N, a = int(input()), list(map(int, input().split()))

total = sum(a)
atual = 0

for k in range(N):
    atual += a[k]
    if atual == total // 2:
        print(k + 1)
        break