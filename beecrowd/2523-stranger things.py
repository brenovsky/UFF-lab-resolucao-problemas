while True:
    try:
        sequence = input('digite o alfabeto: ')
        N = int(input('digite o N: '))
        l = list(map(int, input().split()))

        word = []

        for i in range(N): 
            indice = l[i] - 1
            word.append(sequence[indice])

        print(''.join(map(str, word)))
    except EOFError:
        break