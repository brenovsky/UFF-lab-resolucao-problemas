a = int(input())
b = int(input())
c = int(input())

if a == b or b == c or a == c:
    print('S')
elif a == b + c or b == a + c or c == a + b:
    print('S')
else:
    print('N')