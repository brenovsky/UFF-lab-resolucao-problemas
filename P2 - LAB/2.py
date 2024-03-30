p = input()
c = 0
lista = []

for i in range(len(p)):
    if i == len(p) - 1:
        c += 1
        lista.append(c)
    elif p[i] != ' ':
        c += 1
    else:
        lista.append(c)
        lista.append('-')
        c = 0

print(''.join(map(str, lista)))