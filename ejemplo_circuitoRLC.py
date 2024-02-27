# -*- coding: utf-8 -*-
"""
R = 8 Ohms
L = 15 Henrios
C = 1F


Vc(s)            1
----- = --------------------
Vi(s)    15*s**2  + 8*s + 1

Respuesta a escalón unitario

Vc(s)            1                1                1
----- = -------------------- *  ---- =  -----------------------
Vi(s)    15*s**2  + 8*s + 1       s      15*s**3  + 8*s**2 + s

"""

from scipy import signal
import sympy

t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

"""
Respuesta a Impulso

Recordar que se consideran que todas las condicioes iniciales son cero
osea, el capacitor y demás no tienen carga.
"""

num = [1]
den = [15, 8, 1]
r,p,k = signal.residue(num, den)
print(r,p,k)
print("Unique Roots --> ", end="")
uniq, mult = signal.unique_roots(p)
print(uniq, mult)


f = r[0]*sympy.exp(p[0]*t) + r[1]*sympy.exp(p[1]*t) 
print(f)

p = sympy.plot(f.subs({a: 2}), xlim=(-1, 10), ylim=(0, 1), show=False)
#p[1].line_color = 'red'
p.show()

"""
Respuesta a Escalón Unitario
"""

num = [1]
den = [15, 8, 1, 0]
r,p,k = signal.residue(num, den)
print(r,p,k)
print("Unique Roots --> ", end="")
uniq, mult = signal.unique_roots(p)
print(uniq, mult)


f1 = (r[0]*sympy.exp(p[0]*t) + r[1]*sympy.exp(p[1]*t) + r[2]*sympy.exp(p[2]*t)) * sympy.Heaviside(t)
print(f1)

p = sympy.plotting.plot(f, f1, (t,-0.1,50))
p[1].line_color = 'red'
p.show()