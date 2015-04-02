import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return t*t*t
	
t1 = np.arange(-5.0, 5.0, 1.0)
plt.plot(t1, f(t1))
plt.show()