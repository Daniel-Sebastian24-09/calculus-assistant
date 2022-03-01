from math import sqrt
a = float(input('Type a: '))
b = float(input('Type b: '))
c = float(input('Type c: '))

delta = b**2 - 4 * a * c
bascaraTheoremX= [0, 0, 0]
if delta == 0:
    bascaraTheoremX[0] = -b / (2 * a)
    print(f'x1 = x2 = {bascaraTheoremX[0]:.2f}')
if delta > 0:
    bascaraTheoremX[1] = (-b + sqrt(delta))/ (2 * a)
    bascaraTheoremX[2] = (-b - sqrt(delta))/ (2 * a)
    print(f'x1 = {bascaraTheoremX[1]:.2f}, and x2 = {bascaraTheoremX[2]:.2f}')
if delta < 0:
    print(f"It's not possibible, because delta = {delta} ")