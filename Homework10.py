import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('--------------number 1--------------')

magaz = pd.Series([4.313, 4.338, 4.358, 4.378, 4.4, 4.425, 4.447, 4.468])
print(magaz)
a1 = pd.Series(np.arange(0, 20, 2))
print(a1)
a2 = pd.Series({'Конфет': 1, 'Напитков': 3, 'Хлеба': 5, 'Продавцов': 7})
print(a2)

print('--------------number 2--------------')

slov = pd.Series(np.arange(0, 1, 2))
slovv = pd.Series(np.arange(2, 1, 3))
print(slov, slovv)
a = set.union(set(slov), set(slovv))
b = pd.Series(list(a))
print(b)

print('--------------number 3--------------')

pol = pd.Series({0: 'female',1: 'male',2: 'male',3: 'female',4: 'female',5: 'male',
  6: 'male',7: 'male',8: 'male',9: 'female',10: 'female',11: 'female',12: 'female',
  13: 'female',14: 'male',15: 'male',16: 'male',17: 'male',18: 'male',19: 'female',
  20: 'female',21: 'female',22: 'male',23: 'male',24: 'male',25: 'male',26: 'female',
  27: 'female',28: 'male',29: 'female',30: 'male',31: 'female',32: 'female',
  33: 'male',34: 'female'})

x = pol.value_counts().index
y = pol.value_counts().values
plt.bar(x, y, color=['pink', 'blue'])
plt.xlabel('количество учеников') 
plt.ylabel('пол учеников') 
plt.title('соотношение студентов')
plt.show()