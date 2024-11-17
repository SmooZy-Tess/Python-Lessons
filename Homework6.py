from random import randint

print('--------------------number 5--------------------')

m = [[2, 3], [4, 7], [5, 7], [9, 8]]
con = []
for i in m:
    con.append(sum(i))
print(m[con.index(max(con))], max(con), m[con.index(min(con))], min(con))

print('--------------------number 6--------------------')

def new_matrix(str):
    list = []
    for k in str:
        if k == min(str):
            if min(str) % 2 == 0:
                list.append(0)
            elif min(str) % 2 != 0:
                list.append(1)
        else:
            list.append(k)
    return list


a = int(input('Введите длину матрицы: '))
b = int(input('Введите ширину матрицы: '))
minc = 1000

matrix = [[randint(-50, 50) for i in range(b)] for j in range(a)]
matrix2 = []

for i in matrix:
    matrix2.append(new_matrix(i))

print(matrix)
print(matrix2)