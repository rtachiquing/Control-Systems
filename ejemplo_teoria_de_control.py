"""
Conceptos Básicos de Teoría de Control en Python con SciPy

Control PID

https://pybonacci.org/2013/10/10/teoria-de-control-en-python-con-scipy-i/

"""

from scipy import signal
import matplotlib.pyplot as plt
K = 1
w0 = 1e3 # rad / s
sys1 = signal.lti([K], [1 / w0, 1]) # Creamos el sistema
w, mag, phase = signal.bode(sys1) # Diagrama de bode: frecuencias, magnitud y fase
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
ax1.semilogx(w, mag) # Eje x logarítmico
ax2.semilogx(w, phase) # Eje x logarítmico

"""
print(sys1.zeros, sys1.poles, sys1.gain) # [] [-1000.] 1000.0
print(sys1.A, sys1.B, sys1.C, sys1.D) # [[-1000.]] [[ 1.]] [[ 1000.]] [ 0.]
"""

print(sys1)


sys2 = signal.lti([1, 2], [1, 6, 25]) # H(s) = (s + 2) / (s ** 2 + 6 * s + 25)
w, H = signal.freqresp(sys2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.plot(H.real, H.imag)
ax1.plot(H.real, -H.imag)
ax2.plot(sys2.zeros.real, sys2.zeros.imag, 'o')
ax2.plot(sys2.poles.real, sys2.poles.imag, 'x')
ax2.grid()



m = 1200  # kg
b = 75  # Ns / m
sys_car = signal.lti(1, [m, b])

t, y = signal.step2(sys_car) # Respuesta a escalón unitario
fig, (ax1) = plt.subplots(1, 1)
ax1.plot(t, 2250 * y) # Equivalente a una entrada de altura 2250
ax1.grid()
