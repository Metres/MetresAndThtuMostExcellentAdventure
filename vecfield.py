import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy.integrate import ode
import numpy as np

fig = plt.figure(num=1)
ax=fig.add_subplot(111)

#Vector field
X,Y = np.meshgrid( np.linspace(-2,2,20),np.linspace(0,4,20) )
U = 1
V = np.sqrt(U)*(X**2)
#Normalize arrows
N = np.sqrt(U**2+V**2)  
U2, V2 = U/N, V/N
ax.quiver( X,Y,U2, V2)


plt.xlim([-2,2])
plt.ylim([0,4])
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()
