from scipy.optimize import root
from math import cos
def fun(x):
    return x + cos(x)
myroot = root(fun,0)
print(myroot)
print(myroot.x)

#minimize optimization
#this is a maxima amd minima

from scipy.optimize import minimize
def func(x):
    return x**3+2*x+7
min = minimize(func,0,method = 'BFGS')
#valid methods 'CG' 'BFGS''Newton-CG' 'L-BFGS-B'    'TNC'    'COBYLA'    'SLSQP'
print(min)