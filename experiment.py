#!/usr/bin/env python
# vim: set fileencoding=utf-8

from numpy.polynomial.polynomial import polypow
from numpy import ones, zeros

def diePmf( dice, sides ):
    # Source: http://www.johndcook.com/blog/2013/04/29/rolling-dice-for-normal-samples-python-version/
     
    # Create an array of polynomial coefficients for
    # x + x^2 + ... + x^sides
    p = ones(sides + 1)
    p[0] = 0
    p /= sides
     
    # Extract the coefficients of p(x)**dice and divide by sides**dice
    pmf = polypow(p, dice)
    #cdf = pmf.cumsum()
    
    return pmf

#    import matplotlib.pyplot as plt
#
#    plt.plot(pmf)
#    plt.show()

def sumPmf( p_X, p_Y ):
    R_Z = len(p_X) + len(p_Y) - 1
    result = zeros( R_Z )
    for z in range( R_Z ):
        result[z] = p_Z( z, p_X, p_Y )
    return result

def p_Z( z, p_X, p_Y ):
    p_Z = 0
    for y in range( len(p_Y) ):
        if z-y < len(p_X) and z-y >= 0:
            p_Z += p_X[ z-y ] * p_Y[ y ]
    return p_Z

def cdf( pmf ):
    return pmf.cumsum()
