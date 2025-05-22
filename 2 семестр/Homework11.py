import sys
import timeit

print("--------------Number 1--------------")

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    __slots__ = ("x", 'y', '_z')

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        raise AttributeError("Доступ к координате z запрещен.")

pt3 = Point3D(10, 20, 30)
print(pt3.x, "- x координата")
print(pt3.y, "- y координата")
print(pt3.z, "- z координата")

try:
    pt3.z = 40
except AttributeError as e:
    print("Ошибка изменения координаты:", e)

try:
    pt3.extra = 100
except AttributeError as e:
    print(e)

try:
    print(pt3.__dict__)
except AttributeError as e:
    print("Произошла ошибка:", e)

print("--------------Number 2--------------")

class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlotPoint:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

def timeproccessing():
    normal_points = [NormalPoint(0, 0) for i in range(1000)]
    slot_points = [SlotPoint(0, 0) for i in range(1000)]

    ntime = timeit.timeit("for p in normal_points: p.x += 1", globals=locals())
    stime = timeit.timeit("for p in slot_points: p.x += 1", globals=locals())

    print(f"Время NormalPoint: {ntime} секунд")
    print(f'Время SlotPoint: {stime} секунд')

    print(f"Размер Первого: {sys.getsizeof(normal_points[0])}")
    print(f"Размер Второго: {sys.getsizeof(slot_points[0])}")

timeproccessing()

print("--------------Number 3--------------")

class Student:
    __slots__ = ("name", "age", "grade")

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def avg_grades(students):
    if not students:
        return 0
    else:
        all_grade = sum(student.grade for student in students)
        return all_grade / len(students)
    
students_list = [
    Student("Alice", 20, 5),
    Student("Alexander", 22, 2),
    Student("Kirill", 21, 5),
    Student("Diana", 23, 3)
]

avg_grade = avg_grades(students_list)
print(avg_grade)

print("--------------Number 4--------------")

class Product:
    __slots__ = ("name", "price", "quantity")

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def check_product(products, price_limit):
    list_product = []
    for product in products.values():
        if product.price > price_limit:
            list_product.append(product.name)
        else:
            pass
    return list_product

products = {
    "apple": Product("Apple", 3.00, 100),
    "banana": Product("Banana", 1.50, 200),
    "cherry": Product("Cherry", 5.00, 50),
    "milk": Product("Milk", 2.50, 30),
}

price_limit = 2.00

print(f"Товары превышающие ценой {price_limit}: {check_product(products, price_limit)}")