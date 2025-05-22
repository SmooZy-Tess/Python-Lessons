print("-----------Number 1-----------")
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
    
    def check_t(self, other):
        if not isinstance(other, Fraction):
            raise NotImplemented()
    
    def __eq__(self, other):
        self.check_t(other, Fraction)
        if self.num1 == other.num1 and self.num2 == other.num2:
            return "Дроби равны!"
        
    def __le__(self, other):
        self.check_t(other, Fraction)
        if self.num1 / self.num2 >= other.num1 / other.num2:
            return f"{Fraction(self.num1, self.num2)} >= {Fraction(other.num1, other.num2)}"
        
    def __ge__(self, other):
        self.check_t(other, Fraction)
        if self.num1 / self.num2 <= other.num1 / other.num2:
            return f"{Fraction(self.num1, self.num2)} <= {Fraction(other.num1, other.num2)}" 
        
    def __lt__(self, other):
        self.check_t(other, Fraction)
        if self.num1 / self.num2 <= other.num1 / other.num2:
            return f"{Fraction(self.num1, self.num2)} < {Fraction(other.num1, other.num2)}" 
        
    def __gt__(self, other):
        self.check_t(other, Fraction)
        if self.num1 / self.num2 <= other.num1 / other.num2:
            return f"{Fraction(self.num1, self.num2)} > {Fraction(other.num1, other.num2)}" 
    
    def __hash__(self):
        return hash((self.num1, self.num2))
     
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
f3 = Fraction(9, 12)
print(f"Сложение дробей: {f1 + f2}")
print(f"Вычитание дробей: {f1 - f2}")
print(f"Умножение дробей: {f1 * f2}")
print(f"Деление дробей: {f1 / f2}")
print(f"Сравнение дробей: {f2 == f3}")

print("Хэширование:")
print(f"1. {hash(f1)}")
print(f"2. {hash(f2)}")
print(f"3. {hash(f3)}")
print(f1.value)

# print("-----------Number 2-----------")

# from fractions import Fraction


# class FractionMatrix:
#     def init(self, matrix):
#         if not self._is_valid_matrix(matrix):
#             raise ValueError("Неверный формат матрицы")
#         self._matrix = matrix

#     def _is_valid_matrix(matrix):
#         if not isinstance(matrix, list) or not matrix:
#             return False
#         row_length = len(matrix[0])
#         return all(isinstance(row, list) and len(row) == row_length for row in matrix)

#     def from_list(cls, matrix):
#         return cls(matrix)

#     @property
#     def determinant(self):
#         return self._determinant(self._matrix)

#     def _determinant(self, matrix):
#         if len(matrix) != len(matrix[0]):
#             raise ValueError("Матрица должна быть квадратной для вычисления определителя!")
#         n = len(matrix)
#         if n == 1:
#             return matrix[0][0]
#         if n == 2:
#             return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
#         det = Fraction(0)
#         for c in range(n):
#             minor = [row[:c] + row[c + 1:] for row in matrix[1:]]
#             det += ((-1) ** c) * matrix[0][c] * self._determinant(minor)
#         return det

#     def add(self, other):
#         if not isinstance(other, FractionMatrix):
#             raise ValueError("Можно складывать только с другими матрицами FractionMatrix")
#         if self._dimensions() != other._dimensions():
#             raise ValueError("Размерности матриц не совпадают!")
#         result = [
#             [self._matrix[i][j] + other._matrix[i][j] for j in range(self._columns())]
#             for i in range(self._rows())
#         ]
#         return FractionMatrix(result)

#     def sub(self, other):
#         if not isinstance(other, FractionMatrix):
#             raise ValueError("Можно вычитать только с другими матрицами FractionMatrix")
#         if self._dimensions() != other._dimensions():
#             raise ValueError("Размерности матриц не совпадают")
#         result = [
#             [self._matrix[i][j] - other._matrix[i][j] for j in range(self._columns())]
#             for i in range(self._rows())
#         ]
#         return FractionMatrix(result)

#     def transpose(self):
#         result = [[self._matrix[j][i] for j in range(self._rows())] for i in range(self._columns())]
#         return FractionMatrix(result)

#     def str(self):
#         return "\n".join(" | ".join(str(self._matrix[i][j]) for j in range(self._columns())) for i in range(self._rows()))

#     def _rows(self):
#         return len(self._matrix)

#     def _columns(self):
#         return len(self._matrix[0])

#     def _dimensions(self):
#         return self._rows(), self._columns()


# m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
# m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])

# print("Матрица m1:")
# print(m1)
# print("---------------------")
# print("Матрица m2:")
# print(m2)

# print("Сумма матриц m1 и m2:")
# print(m1 + m2)

# print("Определитель матрицы m1:")
# print(m1.determinant)

# print("Транспонированная матрица m1:")
# print(m1.transpose())