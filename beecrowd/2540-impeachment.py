while True:
    try:

        N = int(input())

        votes = list(map(int, input().split()))

        if sum(votes) >= (2 / 3) * N:
            print('impeachment')
        else:
            print('acusacao arquivada')
            
    except EOFError:
        break