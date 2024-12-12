import math

print('------------number 1------------')

r = int(input())
print(round(2 * math.pi * r, 2))
print(round(math.pi * math.pow(r, 2), 2))

print('------------number 2------------')

x = 10
y = 55
x, y = y, x
print(x, y)

print('------------number 3------------')

L = int(input())
g = 9.81
print((2 * math.pi * math.sqrt(float(L) / g), 2))