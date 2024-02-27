# -*- coding: utf-8 -*-
"""


https://notebook.community/nicoguaro/AdvancedMath/notebooks/sympy/laplace_transform

@author: tachi
"""

import sympy

# Resolviendo ecuación diferencial
# defino las incognitas
x = sympy.Symbol('x')
y = sympy.Function('y')

# expreso la ecuacion
f = 6*x**2 - 3*x**2*(y(x))
print(sympy.Eq(y(x).diff(x), f))

# Resolviendo la ecuación
print(sympy.dsolve(y(x).diff(x) - f))

# definiendo la ecuación
eq = 1.0/2 * (y(x)**2 - 1)

# Condición inicial
ics = {y(0): 2}

# Resolviendo la ecuación
edo_sol = sympy.dsolve(y(x).diff(x) - eq)
print(edo_sol)


C_eq = sympy.Eq(edo_sol.lhs.subs(x, 0).subs(ics), edo_sol.rhs.subs(x, 0))
print(C_eq)

print(sympy.solve(C_eq))

