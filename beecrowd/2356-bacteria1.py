D = input()
S = input()

resistance = False

for i in range(len(S)):
    for j in range(len(D)):
        if S[i] == D[j]:
            resistance = True

if resistance == False:
    print('Resistente')
else:
    print('Nao resistente')