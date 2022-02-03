def electricTension():
    p = float(input('p: '))
    l = float(input('l: '))
    A = float(input('A: '))
    I = float(input('I: '))
    V = p * l/A * I
    return V


print(f'{electricTension()} V')