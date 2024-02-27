# -*- coding: utf-8 -*-
"""
Encontrar zeros, polos y ganancia


https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.tf2zpk.html

"""

from scipy import signal


"""
B(s)         4s^2 + 16s + 12
---- = --------------------------
A(s)    s^4 + 12s^3 + 44s^2 + 48s

Encuentra los zeros 'z', polos 'p', y ganancia 'k'
"""
num = [4, 16, 12]
den = [1, 12, 44, 48, 0]
z, p, k = signal.tf2zpk(num, den)
print(z, p, k)

# Encuentra la ecuación con numerador 'num' y denominador 'den'
num, den = signal.zpk2tf(z, p, k)
print(num, den)

