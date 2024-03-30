escolha = list(map(int, input().split()))
a = 0
b = 0
for i in range(1, 5):
    if escolha[i] >= escolha [i - 1] + 1:
        a += 1
        if a == 4:
            print('C')
            break
    if escolha [i] <= escolha [i - 1] - 1:
        b += 1
        if b == 4:
            print('D')
            break
if a != 4 and b != 4:
    print('N')





#a = 0
#b = 0
#escolha = []
#for i in range(5):
#    escolha.append(int(input()))
#for i in range(1, 5):
#    if escolha[i] >= escolha [i - 1] + 1:
#        a += 1
#        if a == 4:
#            print('C')
#            break
#    if escolha [i] <= escolha [i - 1] - 1:
#        b += 1
#        if b == 4:
#            print('D')
#            break
#if a != 4 and b != 4:
#    print('N')