import numpy as np
import matplotlib.pyplot as plt
from ... import *
from ... import *

# The function for the unknown interest rate problem. x is the percentual interest rate and parameters are set as in lecture 2:
def f(x):
    return 

def df(x):
    return 

# First try bisection:
l=
r= 
kMax = 50
eps_x = 
eps_f = 

 ... = bis( ... )

# Now use newton:
x0=
kMax = 
 ... = Newton( ... )

# Now plot on a semilof (y) scale to see a straight line for bisection:
plt.semilogy( ... ,'-*r')
plt.semilogy( ... ,'-*k')
plt.title('Red: bisection. Black: Newton iteration.')
plt.xlabel('Nr. of iterations')
plt.ylabel('error')
plt.show()
