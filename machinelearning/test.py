from tempfile import TemporaryFile
import numpy as np
x = np.arange(10)
np.savetxt('test.txt', x)
y= np.loadtxt('test.txt')
print(y)

