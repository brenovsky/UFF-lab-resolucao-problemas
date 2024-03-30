def menor(x, y):
    if len(x) > len(y):
        return y
    if len(x) < len(y):
        return x
    return x

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

p1 = input()
p2 = input()

minor = menor(p1, p2)

for i in range(len(minor)):
    if p1[i] != p2[i]:
        if alfabeto.index(p1[i]) < alfabeto.index(p2[i]):
            print(p1)
            print(p2)
            break
        else:
            print(p2)
            print(p1)
            break
else:
    print(p1)
    print(p2)            