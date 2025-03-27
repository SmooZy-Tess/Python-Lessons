from math import gcd

class Fraction:
    def __init__(self, num1, num2):
        if not isinstance(num1, int) and not isinstance(num2, int):
            raise TypeError("Числа должны быть целыми")
        if num2 == 0:
            raise ValueError("Знаменатель не может быть равен 0")
        
        all_del = gcd(num1, num2)
        self.num1 = num1 // all_del
        self.num2 = num2 // all_del

    @property
    def value(self) -> float:
        return round(self.num1 / self.num2, 3)

    def __str__(self):
        return f"{self.num1}/{self.num2}"

    def __add__(self, other):
        print('Метод __add__ обрабатывается...')
        if not isinstance(other, Fraction):
            raise ArithmeticError("Неправильное значение дроби")
        
        new_num1 = self.num1 * other.num2 + other.num1 * self.num2
        new_num2 = self.num2 * other.num2 
        return Fraction(new_num1, new_num2)
    
    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise ArithmeticError("Неправильное значение дроби")
        
        new_num1 = self.num1 * other.num2 - other.num1 * self.num2
        new_num2 = self.num2 * other.num2  
        return Fraction(new_num1, new_num2)
    
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise ArithmeticError("Неправильное значение дроби")
        
        new_num1 = self.num1 * other.num1
        new_num2 = self.num2 * other.num2
        return Fraction(new_num1, new_num2)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise ArithmeticError("Неправильное значение дроби")
        
        new_num1 = self.num1 * other.num2
        new_num2 = self.num2 * other.num1
        return Fraction(new_num1, new_num2)

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1.value)

