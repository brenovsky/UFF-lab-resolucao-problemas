outputs = []
ciclo = True

while(ciclo):
    n = int(input())
    
    if (n == 0):
        ciclo = False

    else:
        for i in range(n):
            answers = list(map(int, input().split())) #cadastrar respostas

            for j in range(5):
                if answers[j] <= 127: #a alternativa é preta?
                    answers[j] = 0
                else: # se não, coloca 1 na lista
                    answers[j] = 1
            
            if (sum(answers) == 4): # se haver 4 brancas, tem uma preta
                indice = answers.index(0) #índice da resposta certa
                
                if (indice == 0):
                    outputs.append("A")

                elif (indice == 1):
                    outputs.append("B")

                elif (indice == 2):
                    outputs.append("C")

                elif (indice == 3):
                    outputs.append("D")

                elif (indice == 4):
                    outputs.append("E")

            else:
                outputs.append("*")

for i in range(len(outputs)):
    print(outputs[i])