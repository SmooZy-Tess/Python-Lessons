import matplotlib.pyplot as plt
import numpy as np


def f(x, alpha, beta):
    return (x**beta + alpha**beta) / x**beta


x_positive = np.linspace(0.01, 5, 1000)
x_negative = np.linspace(-5, -0.01, 1000)
x_small = np.linspace(0.01, 0.5, 100)
x_large = np.linspace(1, 5, 100)
x_neg_large = np.linspace(-5, -1, 100)


plt.figure(figsize=(12, 8))


plt.plot(x_positive, f(x_positive, 1, 1), label='α=1, β=1', color='b')
plt.plot(x_positive, f(x_positive, 2, 1), label='α=2, β=1', color='g')
plt.plot(x_positive, f(x_positive, 1, 2), label='α=1, β=2', color='r')

plt.subplot(1, 1, 1)
plt.plot(x_small, f(x_small, 1, 1), color='b')
plt.plot(x_small, f(x_small, 2, 1), color='g')
plt.plot(x_small, f(x_small, 1, 2), color='r')
plt.xlim(0, 0.5)
plt.ylim(-5, 5)
plt.title('Врезка для малых x')
plt.grid(True)

plt.subplot(1, 1, 1)
plt.plot(x_large, f(x_large, 1, 1), color='b')
plt.plot(x_large, f(x_large, 2, 1), color='g')
plt.plot(x_large, f(x_large, 1, 2), color='r')
plt.xlim(1, 5)
plt.ylim(0, 5)
plt.title('Врезка для больших x')
plt.grid(True)


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графики функции для x > 0')
plt.legend()
plt.grid(True)


plt.savefig('graph_positive.svg')
plt.show()


plt.figure(figsize=(12, 8))


plt.plot(x_negative, f(x_negative, 1, 0.5), label='α=1, β=0.5', color='b')
plt.plot(x_negative, f(x_negative, 1, -0.5), label='α=1, β=-0.5', color='g')
plt.plot(x_negative, f(x_negative, 1, -1.5), label='α=1, β=-1.5', color='r')


plt.subplot(1, 1, 1)
plt.plot(x_neg_large, f(x_neg_large, 1, 0.5), color='b')
plt.plot(x_neg_large, f(x_neg_large, 1, -0.5), color='g')
plt.plot(x_neg_large, f(x_neg_large, 1, -1.5), color='r')
plt.xlim(-5, -1)
plt.ylim(-10, 5)
plt.title('Врезка для x < 0')
plt.axhline(0, color='black', lw=0.5)
plt.grid(True)


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графики функции для x < 0')
plt.legend()
plt.grid(True)


plt.savefig('graph_negative.svg')
plt.show()


plt.figure(figsize=(12, 8))


plt.plot(x_positive, f(x_positive, 1, 0), label='α=1, β=0 (b--)', linestyle='--', color='b')
plt.plot(x_positive, f(x_positive, 1, -1), label='α=1, β=-1 (r--)', linestyle='--', color='r')
plt.plot(x_positive, f(x_positive, 1, 0.5), label='α=1, β=0.5', color='c')
plt.plot(x_positive, f(x_positive, 1, 0.8), label='α=1, β=0.8', color='m')
plt.plot(x_positive, f(x_positive, 1, -0.5), label='α=1, β=-0.5', color='y')
plt.plot(x_positive, f(x_positive, 1, -0.8), label='α=1, β=-0.8', color='orange')
plt.plot(x_positive, f(x_positive, 1, -1.5), label='α=1, β=-1.5', color='purple')
plt.plot(x_positive, f(x_positive, 1, -2.5), label='α=1, β=-2.5', color='pink')


plt.axhline(0, color='black', lw=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Сравнительные графики для α=1')
plt.legend()
plt.grid(True)


plt.savefig('graph_comparison.svg')
plt.show()