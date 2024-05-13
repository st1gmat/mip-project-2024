import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def linearize_diff_eq(f, x, u, t, x0, u0, t0):
    x_sym = sp.symbols('x')
    u_sym = sp.symbols('u')
    t_sym = sp.symbols('t')
    
    f0 = f.subs([(x, x0), (u, u0), (t, t0)])
    A = sp.diff(f, x).subs([(x, x0), (u, u0), (t, t0)])
    B = sp.diff(f, u).subs([(x, x0), (u, u0), (t, t0)])
    
    dxdt_approx = f0 + A * (x_sym - x0) + B * (u_sym - u0)
    
    return dxdt_approx

x, u, t = sp.symbols('x u t')
f = sp.sin(x) + sp.cos(u) * t**2

x0 = 0
u0 = 1
t0 = 2

# линеаризируем
linearized_eq = linearize_diff_eq(f, x, u, t, x0, u0, t0)

print("Символьное решение: ", linearized_eq)

# из символьного выражения сделаем функцию
f_func = sp.lambdify(x, f.subs([(u, u0), (t, t0)]), 'numpy')
linearized_func = sp.lambdify(x, linearized_eq.subs([(u, u0), (t, t0)]), 'numpy')

x_values = np.linspace(-5, 5, 100)
f_values = f_func(x_values)
linearized_values = linearized_func(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, f_values, label='Исходная функция')
plt.plot(x_values, linearized_values, label='Линеаризованная функция')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Исходная и линеаризованная функции')
plt.legend()
plt.grid(True)
plt.show()