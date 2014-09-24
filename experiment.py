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

def constantPmf( value ):
    pmf = zeros( value + 1 )
    pmf[value] = 1.
    return pmf

def generateFill(pmf, limit):
    fill_x = []
    fill_y = []
    for x in range(len(pmf)):
        if x > limit:
            if len(fill_x) == 0:
                fill_x.append( x )
                fill_y.append( 0. )
            fill_x.append( x )
            fill_y.append( pmf[x] )
    return (fill_x, fill_y)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    pmf = sumPmf(
        sumPmf(
            diePmf(4, 6),
            diePmf(3, 4)
        ),
        constantPmf(5)
    )

    (fill_x, fill_y) = generateFill(pmf, 30)

    plt.plot(pmf)
    plt.fill(fill_x, fill_y, "b")
    plt.show()
