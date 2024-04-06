outputs = []
ciclo = True

while(ciclo):

    n = int(input())

    if n == 0:
        ciclo = False
    
    else:
        scores = list(map(int, input().split())) #armazena os scores

        john = sum(scores) #quando john ganha, ele tira 1. ou seja, a quantidade de vezes que ele ganha é a soma da lista
        mary = n - john #para mary, é o complemento

        outputs.append(f'Mary won {mary} times and John won {john} times')

for i in range(len(outputs)):
    print(outputs[i])