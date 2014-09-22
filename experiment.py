#!/usr/bin/env python
# vim: set fileencoding=utf-8

from numpy.polynomial.polynomial import polypow
from numpy import ones

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
