import pandas as pd
import matplotlib.pyplot as plt

file = '/lof/Mall_Customers.csv'
df = pd.read_csv(file, sep=',')
print(df)

print('-----------------number 2-----------------')

Fem = df[df['Genre'] == 'Female']
Femi = sum(Fem['Annual Income (k$)'])/len(Fem)
maxFem = Fem['CustomerID'].where(Fem['Annual Income (k$)'] == max(Fem['Annual Income (k$)'])).dropna()
print(Femi)

print('-----------------number 3-----------------')

Ma = df[df['Genre'] == 'Male']
maxm = Ma['CustomerID'].where(Ma['Annual Income (k$)'] == max(Ma['Annual Income (k$)'])).dropna()
print(maxm.index)

print(maxFem.index)

print('-----------------number 4-----------------')

data = Ma.groupby('Age')['Annual Income (k$)'].mean()
plt.plot(data)
plt.show()

print('-----------------number 5-----------------')

fig, ax = plt.subplots(figsize=(10, 6))

data_m = Ma.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()
data_w = Fem.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()

data_m.plot.bar(color='blue')
data_w.plot.bar(color='pink')
plt.show()