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
