import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return (x-2)**9

def f2(x):
    return (x**9) - (18*x**8) + (144*x**7) - \
           (672*x**6) + (2016*x**5) - (4032*x**4) + \
           (5376*x**3) - (4608*x**2) + (2304*x) - 512

x = np.linspace(1.920, 2.080, 1000)

y1 = f1(x)
y2 = f2(x)

plt.figure()
# f2 visivelmente é mais ruidosa, pois, por performar mais operações de ponto flutuante,
# está sujeita a maiores erros numéricos acumulados.
plt.plot(x, y2, color='orange', label='f2(x)', linewidth=1.5)
plt.plot(x, y1, color='purple', label='f1(x)', linewidth=1.5)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()