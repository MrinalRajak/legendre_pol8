
#legendre polynomial
#(8) integration(-1-->1)(P(n,x)*(1-2*x*t+t**2)**(-.05)) = ((2*t**(n))/(2*n+1))

import numpy as np
from scipy.special import legendre
from scipy.integrate import quad
from scipy.misc import derivative

x=float(input("Enter the x: "))
t=float(input("Enter the t: "))
n=int(input("Enter the n: "))

def f(x):
    return (legendre(n)(x))*(1-2*x*t+t**2)**(-0.5)

LHS=quad(f,-1,1)[0]
RHS=((2*t**(n))/(2*n+1))

print("LHS: ",LHS)
print("RHS: ",RHS)
