"""
Ejercicio de reducción de diagrama de blaques con sympy

"""

from sympy import *
init_printing()

(R, V1, V2, V3, V4, V5, V6, V7, V8, C, 
 G1, G2, G3, H1, H2, H3) = symbols(
     'R, V1, V2, V3, V4, V5, V6, V7, V8, C, G1, G2, G3, H1, H2, H3')

unknowns = V1, V2, V3, V4, V5, V6, V7, V8, C

eqs = [# Blocks
       V2 - G1*V1,
       V4 - G2*V3,
       C - G3*V5,
       V6 - H1*V4,
       V7 - H2*V4,
       V8 - H3*C,
       # Sums
       V1 - (R - V6),
       V3 - (V2 - V7),
       V5 - (V4 + V3 - V8),
       ]

sol = solve(eqs, unknowns)
init_printing()
#print(sol)
pprint(sol)
print()
#print(sol[C].factor())
pprint(sol[C].factor())


"""
Ejercicio 2: El original de la presentación
"""
(R, V1, V2, V3, V4, V5, V6, V7, V8, C, 
 G1, G2, G3, H1, H2, H3) = symbols(
     'R, V1, V2, V3, V4, V5, V6, V7, V8, C, G1, G2, G3, H1, H2, H3')

unknowns = V1, V2, V3, V4, V5, V6, V7, V8, C

eqs = [# Blocks
       V2 - G1*V1,
       V4 - G2*V3,
       C - G3*V5,
       V6 - H3*V5,
       V7 - H1*C,
       V8 - H2*C,
       # Sums
       V1 - (R - V8),
       V3 - (V2 - V6),
       V5 - (V4 - V7),
       ]

sol = solve(eqs, unknowns)
init_printing()
#print(sol)
pprint(sol)
print()
#print(sol[C].factor())
pprint(sol[C].factor())



