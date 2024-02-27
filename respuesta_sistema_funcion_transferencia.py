from scipy import signal
import sympy

t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)


num = [1]
den = [1, 2, 0, 0]
r,p,k = signal.residue(num, den)
print("CASO 1: ", end="")
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


f = 0.5*sympy.exp(-4*t) 
F1 = sympy.laplace_transform(f, t, s, noconds=True)
f1 = sympy.inverse_laplace_transform(F1, s, t)
f2 = 0.5 - f
f3 = (-1/4) + t/2 + (sympy.exp(-2*t)/4)

p = sympy.plot(f.subs({a: 2}), f1.subs({a: 2}), f2.subs({a: 2}), f3.subs({a: 2}), 
               xlim=(-1, 5), ylim=(0, 3), show=False)
p[1].line_color = 'red'
p[2].line_color = 'orange'
p[3].line_color = "purple"
p.show()



from sympy.physics.control.lti import TransferFunction
tf1 = TransferFunction(1, s**2 + 2*s, s)
print(tf1.num)
print(tf1.den)
