""" number 1
x = int(input("Введите стоимость 1 кг конфет: \n"))
for i in range(1, 11):
	print(f"{i}) цена 1 кг конфет = {x * i}")
"""

""" number 2
x = int(input("Вводите числа. Окончить счетчик 0: \n"))
sum = 0
count = 1
while x != 0:
	sum += x
	count += 1
	x = int(input())
print(f"{sum} - сумма введеных чисел, {count} - кол-во введеных чисел")
"""


l =  [1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
b = []
for j in range(1, 1000):
	b.append(hex(j)[2:])
sum = 0
for i in l:
	if type(i) is str:
		if i in b:
			sum += int(i, 16)
		if i.isdigit():
			sum += int(i)
	else:
		sum += i
print(sum)


""" number 4
x = int(input("Ввести кол-во овечек"))
for i in range(1, x + 1):
	if i % 10 == 0 or i % 10 > 5:
		print(f"{i} овечек")
	elif i % 10 == 1:
		print(f"{i} овечка")
	else:
		print(f"{i} овечки")
"""



