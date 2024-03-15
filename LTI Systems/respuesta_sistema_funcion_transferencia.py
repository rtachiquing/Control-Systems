from scipy import signal
import sympy


"""
Ejemplo:
    
d c(t)
------ + 2 c(t) = r(t)
 d t


sC(s) + 2C(s) = R(s)


        C(s)       1
G(s) = ------ = -------
        R(s)     s + 2 

"""
t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

num = [1]
den = [1, 2]
r,p,k = signal.residue(num, den)
print("CASO 1: ", end="")
print(r,p,k)
print("Unique Roots --> ", end="")
uniq, mult = signal.unique_roots(p)
print(uniq, mult, end="")
print()

F = []
k = 0
for i in mult:
    for j in range(i):
        F_fracc = r[k]/((s-p[k])**(j+1)) 
        F.append(F_fracc)
        k += 1

print(F)
    
f_original = sympy.exp(-2*t)
f_conv_impulso = 0
for i in F:
    f_conv_impulso += sympy.inverse_laplace_transform(i, s, t)

print(f_conv_impulso)
print()

plot = sympy.plot(f_original, f_conv_impulso, xlim=(-1, 5), ylim=(0, 3), show=False)
plot[1].line_color = 'red'
plot.show()


"""
Ejemplo:

        C(s)       1
G(s) = ------ = -------
        R(s)     s + 2 

                                                            1
C(s) = {Escalón Unitario = R(s)}  * G(s) = R(s)*G(s) = -----------
                                                        s (s + 2)
"""
num = [1]
den = [1, 2, 0]
r,p,k = signal.residue(num, den)
print("CASO 1: ", end="")
print(r,p,k)
print("Unique Roots --> ", end="")
uniq, mult = signal.unique_roots(p)
print(uniq, mult, end="")
print()

F = []
k = 0
for i in mult:
    for j in range(i):
        F_fracc = r[k]/((s-p[k])**(j+1)) 
        F.append(F_fracc)
        k += 1

print(F)
    

f_conv_esc_unit = 0
for i in F:
    f_conv_esc_unit += sympy.inverse_laplace_transform(i, s, t)

print(f_conv_esc_unit)
print()

plot = sympy.plot(f_original, f_conv_impulso, f_conv_esc_unit, 
                  xlim=(-1, 5), ylim=(0, 3), show=False)
plot[1].line_color = 'red'
plot[2].line_color = 'orange'
plot.show()

"""
Ejemplo:

        C(s)       1
G(s) = ------ = -------
        R(s)     s + 2 

                                                           1
C(s) = {Rampa Unitaria = R(s)}  * G(s) = R(s)*G(s) = -------------
                                                      s^2 (s + 2)
"""
num = [1]
den = [1, 2, 0, 0]
r,p,k = signal.residue(num, den)
print("CASO 2: ", end="")
print(r,p,k)
print("Unique Roots --> ", end="")
uniq, mult = signal.unique_roots(p)
print(uniq, mult, end="")
print()

F = []
k = 0
for i in mult:
    for j in range(i):
        F_fracc = r[k]/((s-p[k])**(j+1)) 
        F.append(F_fracc)
        k += 1

print(F)


f_conv_ramp_unit = 0
for i in F:
    f_conv_ramp_unit += sympy.inverse_laplace_transform(i, s, t)

print(f_conv_ramp_unit)
print()

plot = sympy.plot(f_original, f_conv_impulso, f_conv_esc_unit, f_conv_ramp_unit,
                  xlim=(-1, 3), ylim=(0, 1.5), show=False)
plot[1].line_color = 'red'
plot[2].line_color = 'orange'
plot[3].line_color = 'purple'
plot.show()


"""
Última muestra mostrando las funciones antes de Cero
"""

f2 = 0.5 - 0.5*sympy.exp(-2*t)
f3 = 0.5*t - 0.25 + 0.25*sympy.exp(-2*t) 

plot = sympy.plot(f_original, f2, f3,
                  xlim=(-1, 3), ylim=(0, 1.5), show=False)
plot.show()


"""
El siguiente ejercicio es:
    
             s
G(s) = -----------------
        (s + 4) (s + 8)
        

Respuesta a Escalón Unitari0:
                s
C(s) = -------------------
        s (s + 4) (s + 8)


Respuesta a Rampa Unitaria:
                s
C(s) = ---------------------
        s^2 (s + 4) (s + 8)
    

         1          1                  1
c(t) = -----  -  ------- e^(-4t) +  ------ e^(-8t)
        32          16                32

"""
num = [1, 0]
den = [1, 12, 32]
r,p,k = signal.residue(num, den)
print("CASO 1: ", end="")
print(r,p,k)
print("Unique Roots --> ", end="")
uniq, mult = signal.unique_roots(p)
print(uniq, mult, end="")
print()

F = []
k = 0
for i in mult:
    for j in range(i):
        F_fracc = r[k]/((s-p[k])**(j+1)) 
        F.append(F_fracc)
        k += 1

f_impulso = 0
for i in F:
    f_impulso += sympy.inverse_laplace_transform(i, s, t)

print(f_impulso)

num = [1, 0]
den = [1, 12, 32, 0]
r,p,k = signal.residue(num, den)
print("CASO 1: ", end="")
print(r,p,k)
print("Unique Roots --> ", end="")
uniq, mult = signal.unique_roots(p)
print(uniq, mult, end="")
print()

F = []
k = 0
for i in mult:
    for j in range(i):
        F_fracc = r[k]/((s-p[k])**(j+1)) 
        F.append(F_fracc)
        k += 1

f_escalon = 0
for i in F:
    f_escalon += sympy.inverse_laplace_transform(i, s, t)

print(f_escalon)

num = [1, 0]
den = [1, 12, 32, 0, 0]
r,p,k = signal.residue(num, den)
print("CASO 1: ", end="")
print(r,p,k)
print("Unique Roots --> ", end="")
uniq, mult = signal.unique_roots(p)
print(uniq, mult, end="")
print()

F = []
k = 0
for i in mult:
    for j in range(i):
        F_fracc = r[k]/((s-p[k])**(j+1)) 
        F.append(F_fracc)
        k += 1

f_rampa = 0
for i in F:
    f_rampa += sympy.inverse_laplace_transform(i, s, t)

print(f_rampa)

plot = sympy.plot(f_impulso, f_escalon, f_rampa,
                  xlim=(-1, 1), ylim=(0, 1), show=False)
plot[0].line_color = 'red'
plot[1].line_color = 'orange'
plot[2].line_color = 'purple'
plot.show()
