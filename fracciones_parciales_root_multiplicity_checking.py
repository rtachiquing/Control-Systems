from scipy import signal
import sympy

t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

"""
Caso 1: Raíces del denominador son reales y distintas
"""

num = [2]
den = [1, 3, 2]
r,p,k = signal.residue(num, den)
print("CASO 1: ", end="")
print(r,p,k)
print("Unique Roots --> ", end="")
print(signal.unique_roots(p))

F = []
for i in range(len(r)):
    F_fracc = r[i]/(s-p[i]) 
    F.append(F_fracc)

for i in F:
    print(sympy.inverse_laplace_transform(i, s, t), end="")
    print(" (+/-) ", end="")
print()

"""
Caso 2: Raíces del denominador son reales y repetidas
"""
num = [2]
den = [1, 5, 8, 4]
r,p,k = signal.residue(num, den)
print("CASO 2: ", end="")
print(r,p,k)
print("Unique Roots --> ", end="")
uniq, mult = signal.unique_roots(p)
print(uniq, mult, end="")

F = []
for i in range(len(uniq)):
    for j in range(mult[i],0,-1):
        F_fracc = r[i]/((s-p[i]))**j 
        F.append(F_fracc)
    
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
print("CASO 3: ", end="")
print(r,p,k)
uniq, mult = signal.unique_roots(p)
print(uniq, mult, end="")

F = []
for i in range(len(r)):
    F_fracc = r[i]/(s-p[i]) 
    F.append(F_fracc)

for i in F:
    print(sympy.inverse_laplace_transform(i, s, t), end="")
    print(" (+/-) ", end="")
print()

