import numpy as np
import matplotlib.pyplot as plt

xvals = np.linspace(1, 10**4) 
yvals = xvals*np.log10(xvals) # Evaluate function on xvals
#plt.plot(xvals, yvals) # Create line plot with yvals against xvals
#yvals = xvals ** 2 # Evaluate function on xvals
yvals = xvals **2 - yvals
plt.plot(xvals, xvals*np.log10(xvals), 'r--') # Create line plot with yvals against xvals
plt.plot(xvals, 10**8*xvals, 'b--')
plt.plot(xvals, 1.000001**xvals, 'g--')
plt.show() # Show the figure

f1(n) = n
0.999999 log n
f2(n) = 10000000n
f3(n) = 1.000001n
f (n) = n
