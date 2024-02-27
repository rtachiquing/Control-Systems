# -*- coding: utf-8 -*-
"""
Laplace Transforms
https://notebook.community/nicoguaro/AdvancedMath/notebooks/sympy/laplace_transform

simpy installation
https://docs.sympy.org/latest/install.html#installation


"""

import sympy
sympy.init_printing()

t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

f1 = sympy.exp(-a*t)
f2 = sympy.exp(a*t)
print(f1)

print(sympy.laplace_transform(f1, t, s))

print(sympy.laplace_transform(t**2, t, s))
print(sympy.laplace_transform(t**4, t, s, noconds = True))
print(sympy.laplace_transform(f2, t, s, noconds = True))
print(sympy.laplace_transform(f1 * t**2, t, s, noconds = True))


"""
Inversa de Laplace
"""

fun = 1/((s-2)*(s-1)**2)
print(sympy.inverse_laplace_transform(fun, s, t))

fun = (1/s) - (2/(s+4)) + (1/(s+8))
print(sympy.inverse_laplace_transform(fun, s, t))

