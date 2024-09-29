print("-------------number1-------------")

n = int(input("Введите число от 1 до 100: \n"))
sum = 0
for i in range(1, n+1):
	sum += i**3
print(sum)

print("-------------number2-------------")

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num2 = []
for i in num1:
	for j in range(1, 10):
		if i*j < 10:
			num2.append(" " + str(i * j))
		else:
			num2.append(str(i * j))
	print(*num2)
	num2 = []

print("-------------number2*-------------")

for i in range(9, 0, -1):
	print(*range(i, i*10, i))
