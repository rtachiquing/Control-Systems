"""
Fracciones Parciales
"""

from scipy import signal

"""
                    32                         32
F1(s) = -------------------------- = ----------------------
         s * (s^2 + 12s + 32)         s^3 + 12s^2 + 32s
"""
num = [32]
den = [1, 12, 32, 0]
r, p, k = signal.residue(num, den)
print(r, p, k)
print()

"""
Siguiente es el mismo ejemplo, pero con el módulo
sympy para expandir la ecuación
"""
from sympy.physics.control.lti import TransferFunction
import sympy

s = sympy.symbols('s')
G1 = TransferFunction(32, s * ( s**2 + 12*s + 32 ), s)
print(G1)
print(G1.expand())
print(G1.poles(), G1.zeros())
print()

"""
También podemos realizar su propia inversa con el siguiente ejemplo
"""
num, den = signal.invres(r, p, k)
print(num, den)
print()

"""
Caso 1: Raíces del denominador son reales y distintas
"""

num = [2]
den = [1, 3, 2]
r,p,k = signal.residue(num, den)
print("CASO 1: ", end="")
print(r,p,k)
print()

Fp1 = r[0]/(s-p[0])
Fp2 = r[1]/(s-p[1])
F = Fp1 + Fp2

t = sympy.symbols('t')
f = sympy.inverse_laplace_transform(F, s, t)
print(f)
print()

"""
Caso 2: Raíces del denominador son reales y repetidas
"""
num = [2]
den = [1, 5, 8, 4]
r,p,k = signal.residue(num, den)
print("CASO 2: ", end="")
print(r,p,k)
print()

print("Unique Roots --> ", end="")
print(signal.unique_roots(p))
root, multiplicity = signal.unique_roots(p)

F = []
for i in range(len(root)):
    for j in range(multiplicity[i]):
        F_fracc = r[i]/((s-root[i])**(j+1)) 
        F.append(F_fracc)

print(F)

t = sympy.symbols('t')
for i in F:
    print(sympy.inverse_laplace_transform(i, s, t), end="")
    print(" (+/-) ", end="")
print()

"""
Caso 3: Raíces del denominador son complejas o imaginarias
"""
num = [3]
den = [1, 2, 5, 0]
r,p,k = signal.residue(num, den)
print()
print("CASO 3: ")
print(r,p,k)

root, multiplicity = signal.unique_roots(p)
print(root, multiplicity)

F = []
for i in range(len(root)):
    for j in range(multiplicity[i]):
        F_fracc = r[i]/((s-root[i])**(j+1)) 
        F.append(F_fracc)

print(F)

t = sympy.symbols('t')
for i in F:
    print(sympy.inverse_laplace_transform(i, s, t), end="")
    print(" (+/-) ", end="")
print()
