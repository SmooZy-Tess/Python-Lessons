print('--------------------number 5--------------------')

matrix = [[2, 3], [4, 7], [5, 7], [9, 8]]
s = []
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print(matrix[s.index(max(s))], max(s), matrix[s.index(min(s))], min(s))

print('--------------------number 6--------------------')