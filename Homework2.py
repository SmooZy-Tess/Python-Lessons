x, y = input("Введите числа через пробел: \n").split()
if x.isdigit() and y.isdigit():
    x, y = map(int, (x, y))
    if y != 0:
        print("Результат деления:", x/y)
    else:
        print("Деление на ноль!")
else:
    print("Вводи целые числа!")

print("-------------number2------------")

summa = input("Введите стоимость покупок в рублях: \n")
if summa.isdigit():
    summa = int(summa)
    if summa > 20:
        discount = summa * 0.65
        print(f"{discount} руб. - конечная цена, {summa - discount} руб. - скидка")
    else:
        print(f"{summa} руб. - конечная цена, {0} руб. - скидка")
else:
    print("Введи стоимость покупок в целом значении!!!")

print("-------------number3------------")

""" number 3
number = input("Введите число от 1 до 12: \n")
Months = ["Январь - Зима", "Февраль - Зима", "Март - Весна", "Апрель - Весна", "Май - Весна", "Июнь - Лето", "Июль - Лето", \
          "Август - Лето", "Сентябрь - Осень", "Октябрь - Осень", "Ноябрь - Осень", "Декабрь - Зима"]
if number.isdigit():
    number = int(number)
    if number >= 1 and number <= 12:
        print(Months[number-1])
    else:
        print("Такого не существует. Всего 12 месяцев в году!")
else:
    print("Введи целое число от 1 до 12!!!")
"""

number = input("Введите число от 1 до 12: \n")
if number.isdigit() or number > "12" or number < "1":
    number = int(number)
    if number <= 2 or number == 12:
        
        print("Зима")
    elif number == 3 or number == 4 or number == 5:
        print("Весна")
    elif number == 6 or number == 7 or number == 8:
        print("Лето")
    else:
        print("Осень")
else:
    print("Введи целое число от 1 до 12!!!")