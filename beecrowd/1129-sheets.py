outputs = []
while(True):
    n = int(input())
    
    if (n == 0):
        break

    for i in range(n):
        answers = list(map(int, input().split())) #cadastrar respostas

        black = 0 #quantidade de pretos identificados (declaracao)
        for j in range(5):
            if answers[j] <= 127: #a alternativa é preta? se sim, adiciona 1 no contador
                black += 1
                if black > 1: # se contador > 1, significa que há mais de uma alternativa marcada (invalido)
                    outputs.append("*") #insere asterisco
                    del(outputs[-2]) #apaga a letra que inserimos no outputs.append(j)
                    break #quebra o loop
            
                outputs.append(j)

for i in range(len(outputs)):
    if outputs[i] == 0:
        outputs[i] = "A"

    if outputs[i] == 1:
        outputs[i] = "B"

    if outputs[i] == 2:
        outputs[i] = "C"

    if outputs[i] == 3:
        outputs[i] = "D"

    if outputs[i] == 4:
        outputs[i] = "E"

print(outputs)