posicao = list(map(int, input().split()))

janela = [0] * 600

for i in range(len(posicao)):
    janela[posicao[i] : posicao[i] + 200] = [1] * 200

print((600 - sum(janela)) * 100)

#print(janela.count(0) * 100)



#solução de bruno
#pos = ['0' for i in range(600)]
#j1 = int(input())
#j2 = int(input())
#j3 = int(input())
#for i in range(200):
#    pos[j1+i]='1'
#    pos[j2+i]='1'
#    pos[j3+i]='1'
#print(pos.count('0') * 100)