import numpy as np
from scipy.signal import convolve
from scipy import signal

#The input sequences
#sequence1 = np.array([1, 2, 3, 4])
#sequence2 = np.array([2, 1])
sequence1 = [1, 2, 3, 4] # x^3 + 2x^2 + 3x + 4 
sequence2 = [2, 1] # 2x + 1

#Performing convolution
"""
Convolución de polinomios - vectores

2x^4 + 4x^3 + 6x^2 + 8x + x^3 + 2x^2 + 3x + 4 = 2x^4 + 5x^3 + 8x^2 + 11x + 4
"""
result = convolve(sequence1, sequence2, mode='full') 

#Printing the result
print("Result of Convolution:", result)

"""
Convolución de ecuaciones - señales

https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html
"""

sig = np.repeat([0, 1, 0], 100)
win = signal.windows.hann(50)
filtered = signal.convolve(sig, win, mode='same') / sum(win)

import matplotlib.pyplot as plt
fig, (ax_orig, ax_win, ax_filt) = plt.subplots(3, 1, sharex=True)
ax_orig.plot(sig)
ax_orig.set_title('Original pulse')
ax_orig.margins(0, 0.1)
ax_win.plot(win)
ax_win.set_title('Filter impulse response')
ax_win.margins(0, 0.1)
ax_filt.plot(filtered)
ax_filt.set_title('Filtered signal')
ax_filt.margins(0, 0.1)
fig.tight_layout()
fig.show()