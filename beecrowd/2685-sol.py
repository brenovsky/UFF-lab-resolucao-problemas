M = int(input())
if (M >= 0 and M < 90) or M == 360:
    print('Bom Dia!!')
elif M >= 90 and M < 180:
    print('Bom Tarde!!')
elif M >= 180 and M < 270:
    print('Bom Noite!!')
elif M >= 270 and M < 360:
    print('De Madrugada!!')