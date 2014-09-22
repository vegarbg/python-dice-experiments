#!/usr/bin/env python
# vim: set fileencoding=utf-8

# Source: http://www.johndcook.com/blog/2013/04/29/rolling-dice-for-normal-samples-python-version/
from numpy.polynomial.polynomial import polypow
from numpy import ones
 
sides = 6
dice = 3
 
# Create an array of polynomial coefficients for
# x + x^2 + ... + x^sides
p = ones(sides + 1)
p[0] = 0
p /= sides
 
# Extract the coefficients of p(x)**dice and divide by sides**dice
pmf = polypow(p, dice)
cdf = pmf.cumsum()

import matplotlib.pyplot as plt

plt.plot(pmf)
plt.show()
