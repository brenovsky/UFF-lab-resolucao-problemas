N = int(input())
pomekon = []
for i in range(N):
    catch = input()
    if catch not in pomekon:
        pomekon.append(catch)
print(f'Falta(m) {151 - len(pomekon)} pomekon(s).')