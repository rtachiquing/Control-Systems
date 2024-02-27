# -*- coding: utf-8 -*-
"""
Laplace Transforms with SymPy

https://dynamics-and-control.readthedocs.io/en/latest/1_Dynamics/3_Linear_systems/Laplace%20transforms.html

"""

import sympy

import matplotlib.pyplot as plt


t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

f = sympy.exp(-a*t)
f
print(f)

print(sympy.integrate(f*sympy.exp(-s*t), (t, 0, sympy.oo)))
print("")


F = sympy.laplace_transform(f, t, s, noconds=True)
print(F)

def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)

def invL(F):
    return sympy.inverse_laplace_transform(F, s, t)

print(invL(F))

print(sympy.Heaviside(t))
sympy.plot(sympy.Heaviside(t))

print(invL(F).subs({a: 2}))
p = sympy.plot(f.subs({a: 2}), invL(F).subs({a: 2}),
               xlim=(-1, 4), ylim=(0, 3), show=False)
p[1].line_color = 'red'
p.show()


#----------
omega = sympy.Symbol('omega', real=True)
exp = sympy.exp
sin = sympy.sin
cos = sympy.cos
functions = [1,
         t,
         exp(-a*t),
         t*exp(-a*t),
         t**2*exp(-a*t),
         sin(omega*t),
         cos(omega*t),
         1 - exp(-a*t),
         exp(-a*t)*sin(omega*t),
         exp(-a*t)*cos(omega*t),
         ]

print("")
print(functions)
print("")
Fs = [L(f) for f in functions]
print(Fs)




