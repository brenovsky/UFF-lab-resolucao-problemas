cartas = list(map(int, input().split()))

if cartas[0] < cartas[1] < cartas[2] < cartas[3] < cartas[4]:
    print('C')
elif cartas[0] > cartas[1] > cartas[2] > cartas[3] > cartas[4]:
    print('D')
else:
    print('N')