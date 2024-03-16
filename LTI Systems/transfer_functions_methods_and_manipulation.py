"""

Funciones de Transferencia aplicación directa gracias a métodos
Siplificación y más aplicaciones

https://docs.sympy.org/latest/modules/physics/control/lti.html

"""


from sympy.abc import s, a
from sympy.physics.control.lti import TransferFunction
tf1 = TransferFunction(s + a, s**2 + s + 1, s)
print(tf1)
print(tf1.num)
print(tf1.den)
print(tf1.var)
print(tf1.args)


"""
Any complex variable can be used for var.
"""
import sympy
p = sympy.symbols('p')

tf2 = TransferFunction(a*p**3 - a*p**2 + s*p, p + a**2, p)
print(tf2)
tf3 = TransferFunction((p + 3)*(p - 1), (p - 1)*(p + 5), p)
print(tf3)

"""
To negate a transfer function the - operator can be prepended:
"""
tf4 = TransferFunction(-a + s, p**2 + s, p)
print(-tf4)
tf5 = TransferFunction(s**4 - 2*s**3 + 5*s + 4, s + 4, s)
print(-tf5)


"""
You can take the integer power of a transfer function using the ** operator:
"""
tf7 = TransferFunction(s + a, s - a, s)
print(tf7**3)
print(tf7**0)
tf8 = TransferFunction(p + 4, p - 3, p)
print(tf8**-1)


"""
Addition, subtraction, and multiplication of transfer functions can form 
unevaluated Series or Parallel objects.
"""
print()
tf9 = TransferFunction(s + 1, s**2 + s + 1, s)
tf10 = TransferFunction(s - p, s + 3, s)
tf11 = TransferFunction(4*s**2 + 2*s - 4, s - 1, s)
tf12 = TransferFunction(1 - s, s**2 + 4, s)
print(tf9 + tf10)
print(tf10 - tf11)
print(tf9 * tf10)
print(tf10 - (tf9 + tf12))
print(tf10 - (tf9 * tf12))
print(tf11 * tf10 * tf9)
print(tf9 * tf11 + tf10 * tf12)
print((tf9 + tf12) * (tf10 + tf11))

"""
These unevaluated Series or Parallel objects can convert into the 
resultant transfer function using .doit() method or by .rewrite(TransferFunction).
"""
print()
print(((tf9 + tf10) * tf12).doit())
print((tf9 * tf10 - tf11 * tf12).rewrite(TransferFunction))

"""
Expansión de las ecuaciones
"""
print()
tf_sol1 = ((tf9 + tf10) * tf12).doit()
print(tf_sol1.expand())


"""
Creates a new TransferFunction efficiently from a rational expression.
"""
print()
expr1 = (s + 5)/(3*s**2 + 2*s + 1)
tf1 = TransferFunction.from_rational_expression(expr1)
print(tf1)
expr2 = (a*p**3 - a*p**2 + s*p)/(p + a**2)  # Expr with more than one variables
tf2 = TransferFunction.from_rational_expression(expr2, p)
print(tf2)


"""
In case of conflict between two or more variables in a expression, 
SymPy will raise a ValueError, if var is not passed by the user.
"""
tf3 = TransferFunction.from_rational_expression(10, s)
print(tf3)

"""
Propiedades de numeradores, variable compleja del sistema, polos y zeros
"""
s = sympy.symbols('s')
G1 = TransferFunction(32, s * ( s**2 + 12*s + 32 ), s)
print(G1)
print(G1.expand())
print(G1.poles(), G1.zeros())
print(G1.var)
print()


"""
A class for representing a series configuration of SISO systems 
(Single Imput-Single Output).
"""

from sympy.physics.control.lti import Series, Parallel
b = sympy.symbols('b')

print()
tf1 = TransferFunction(a*p**2 + b*s, s - p, s)
tf2 = TransferFunction(s**3 - 2, s**4 + 5*s + 6, s)
tf3 = TransferFunction(p**2, p + s, s)
S1 = Series(tf1, tf2)
print(S1)
#print(S1.var)
S2 = Series(tf2, Parallel(tf3, -tf1))
print(S2)
#print(S2.var)
S3 = Series(Parallel(tf1, tf2), Parallel(tf2, tf3))
print(S3)
#print(S3.var)
S4 = Series(tf1, tf2, -tf3)
print(S4.doit())
S5 = Series(tf2, Parallel(tf1, -tf3))
print(S5.doit())


"""
Feedback
A class for representing closed-loop feedback interconnection between two SISO input/output systems.
"""
from sympy.physics.control.lti import Feedback
plant = TransferFunction(3*s**2 + 7*s - 3, s**2 - 4*s + 2, s)
controller = TransferFunction(5*s - 10, s + 7, s)
F1 = Feedback(plant, controller)
print()
print(F1)
#print(F1.var)
#print(F1.args)
#You can get the feedforward and feedback path systems by using .sys1 and .sys2 respectively.
print(F1.sys1)
print(F1.sys2)

"""
You can get the resultant closed loop transfer function obtained by negative 
feedback interconnection using .doit() method.
"""
print()
print(F1.doit())
G = TransferFunction(2*s**2 + 5*s + 1, s**2 + 2*s + 3, s)
C = TransferFunction(5*s + 10, s + 10, s)
F2 = Feedback(G*C, TransferFunction(1, 1, s))
print(F2.doit())

#To negate a Feedback object, the - operator can be prepended:
print(-F1)
print(-F2)


"""
Extención del método doit(), kwargs "cancel=True" and "expand=True"
Returns the resultant transfer function obtained by the feedback interconnection

Use kwarg expand=True to expand the resultant transfer function. 
Use cancel=True to cancel out the common terms in numerator and denominator.

"""
plant = TransferFunction(3*s**2 + 7*s - 3, s**2 - 4*s + 2, s)
controller = TransferFunction(5*s - 10, s + 7, s)
F1 = Feedback(plant, controller)
print()
print(F1.doit())
print(F1.doit(cancel=True, expand=True))
#print(F1.doit(expand=True))
G = TransferFunction(2*s**2 + 5*s + 1, s**2 + 2*s + 3, s)
F2 = Feedback(G, TransferFunction(1, 1, s))
print()
print(F2.doit())

print(F2.doit(cancel=True, expand=True))
#print(F2.doit(expand=True))













