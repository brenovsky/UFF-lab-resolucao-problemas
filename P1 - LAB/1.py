N = int(input())
I = int(input())
F = int(input())

somas = []
vetor = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if vetor[i] + vetor[j] >= I and vetor[i] + vetor[j] <= F and i != j:
            somas.append([vetor[i], vetor[j]])
            
print(len(somas) // 2)