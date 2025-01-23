import numpy as np
import matplotlib.pyplot as plt
from bisection import *
from newton import *

# The function for the unknown interest rate problem. x is the percentual interest rate and parameters are set as in lecture 2:
def f(x):
    return 1-(1/((1+x)**12))-10*x

def df(x):
    return (12/((1+x)**13))-10

# First try bisection:
l=0.02
r= 0.04
kMax = 50
eps_x = 1.0e-10
eps_f = 1.0e-10

bis_iterations, bis_conv = bis(f,l,r,eps_x,eps_f,kMax)

print('_____________')

# Now use newton:
x0=0.04
kMax = 20
newton_iterations, newton_conv = Newton(f,df,x0,eps_x,eps_f,kMax)

bis_error = [inside[1] for inside in bis_iterations]
newton_error = [inside[1] for inside in newton_iterations]

# Now plot on a semilof (y) scale to see a straight line for bisection:
plt.semilogy(bis_error,'-*r')
plt.semilogy(newton_error,'-*k')
plt.title('Red: bisection. Black: Newton iteration.')
plt.xlabel('Nr. of iterations')
plt.ylabel('error')
plt.show()