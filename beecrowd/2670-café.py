#A1 = int(input('quantas pessoas trabalham no andar 1? '))
#A2 = int(input('quantas pessoas trabalham no andar 2? '))
#A3 = int(input('quantas pessoas trabalham no andar 3? '))
#minutos = []
#minutos.append(2 * A2 + 4 * A3) #no A1
#minutos.append(2 * A1 + 2 * A3) #no A2
#minutos.append(2 * A2 + 4 * A1) #no A3
#print(min(minutos))

#código generalizado para n andares
def modulo(x): #praticando criar função
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0    

n = int(input('digite a quantidade de andares: '))
andar = []
minutos = []
for i in range(n):
    andar.append(int(input(f'quantas pessoas tem no {i + 1}° andar?')))
for cafe in range(n):
    tempo = 0
    for i in range(n):
        tempo += andar[i] * 2 * modulo(i - cafe)
    minutos.append(tempo)

print(f'a menor quantidade possível de minutos gastos é {min(minutos)}')
