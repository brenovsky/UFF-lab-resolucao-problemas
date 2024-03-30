#código certo, porém time limit exceeded no beecrowd :/
N = int(input())

ordem = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
a = 0
b = 0

for i in range(N):
    cartas = list(map(int, input().split()))
    x = 0
    y = 0
    for j in range(3):
        A = cartas[j]
        B = cartas[j + 3]
        for k in range(len(ordem)):
            if A == ordem[k]:
                r1 = ordem.index(A)
                break
        for k in range(len(ordem)):
            if B == ordem[k]:
                r1 = ordem.index(B)
                break
            if A >= B:
                x += 1
            else:
                y += 1
    if x >= y:
        a += 1
    else: 
        b += 1

print(a, b)
