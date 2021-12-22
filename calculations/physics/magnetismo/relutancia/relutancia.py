from math import pi
l = float(input('l: '))
S = float(input('S: '))
ur= float(input('ur: '))
u = ur * 4 * pi * 10**-7

Rel = (l) / (u * S)
print(f'Rel = {Rel:.2f}')
