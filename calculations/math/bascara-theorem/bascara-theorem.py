from math import sqrt
a = float(input('Type a: '))
b = float(input('Type b: '))
c = float(input('Type c: '))

delta = b**2 - 4 * a * c

if delta == 0:
    bascaraTheorem = -b / (2 * a)
    print(f'x1 = x2 = {bascaraTheorem:.2f}')
if delta > 0:
    bascaraTheoremX1 = (-b + sqrt(delta))/ (2 * a)
    bascaraTheoremX2 = (-b - sqrt(delta))/ (2 * a)
    print(f'x1 = {bascaraTheoremX1:.2f}, and x2 = {bascaraTheoremX2:.2f}')
if delta < 0:
    print(f"It's not possibible, because delta = {delta} ")