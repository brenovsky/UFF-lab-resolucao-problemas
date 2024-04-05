N = int(input())
victory = []

while (N > 0):
    M1, x, V1 = map(str, input().split())
    V2, x, M2 = map(str, input().split())

    M1, M2 = int(M1), int(M2)
    V1, V2 = int(V1), int(V2)

    if M1 + M2 == V1 + V2: #tie
        if (V1 > M2):
            victory.append("Time 2")
        elif (V1 < M2):
            victory.append("Time 1")
        else:
            victory.append("Penaltis")
    
    else: #if not tie
        if (M1 + M2 > V1 + V2):
            victory.append("Time 1")
        else: 
            victory.append("Time 2")

    N -= 1

for i in range(len(victory)):
    print(victory[i])
