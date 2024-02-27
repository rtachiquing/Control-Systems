"""
Desarrollo de fracciones simples

    https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.residue.html

scipy install --> https://scipy.org/install/

"""

from scipy import signal

"""
B(s)    2s^3 + 5s^2 + 3s + 6
---- = ----------------------
A(s)    s^3 + 6s^2 + 11s + 6
"""
"""
num = [2, 5, 3, 6]
den = [1, 6, 11, 6]
r, p, k = signal.residue(num, den) 
print(r, p, k)

num, den = signal.invres(r, p, k)
print(num, den)

# El siguiente ejercicio arroja números complejos, solo se considera el real. 
# El coeficiente de la segunda fracción es 7.77e-16, notese que es aprox = 0.
num = [0,1,2,3]
den = [1,3,3,1]
r,p,k = signal.residue(num, den)
print(r,p,k)

num, den = signal.invres(r, p, k)
print(num, den)
"""

"""
                 32
F1(s) = ----------------------
          s^3 + 12s^2 + 32s
"""
num = [32]
den = [1, 12, 32, 0]
r, p, k = signal.residue(num, den) 
print(r, p, k)

num, den = signal.invres(r, p, k)
print(num, den)

"""
# ---- Caso 1
num = [2]
den = [1, 3, 2]
r,p,k = signal.residue(num, den)
print(r,p,k)

num, den = signal.invres(r,p,k)
print(den, num)
"""

from scipy import signal
import sympy


"""
                 32
F1(s) = ----------------------
          s^3 + 12s^2 + 32s
"""
num = [32]
den = [1, 12, 32, 0]
r, p, k = signal.residue(num, den) 
print(r, p, k)

num, den = signal.invres(r, p, k)
print(num, den)



"""
Caso 1: Raíces del denominador son reales y distintas
"""

num = [2]
den = [1, 3, 2]
r,p,k = signal.residue(num, den)
print("CASO 1: ", end="")
print(r,p,k)

"""
Caso 2: Raíces del denominador son reales y repetidas
"""
num = [2]
den = [1, 5, 8, 4]
r,p,k = signal.residue(num, den)
print("CASO 2: ", end="")
print(r,p,k)


"""
Caso 3: Raíces del denominador son complejas o imaginarias
"""
num = [3]
den = [1, 2, 5, 0]
r,p,k = signal.residue(num, den)
print("CASO 3: ", end="")
print(r,p,k)


