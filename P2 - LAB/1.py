N = int(input())
X = list(map(int, input().split()))

print(f'Menor valor: {min(X)}')
print(f'Posição: {X.index(min(X))}')