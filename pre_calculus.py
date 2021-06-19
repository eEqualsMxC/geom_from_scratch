from __future__ import  annotations # Define Error
from algebra import power
from algebra import factorial
from typing import Union
from constants import PI

def degree_to_radian(deg: Union[float, int]) -> float:
    """Convert Degrees Decimal to Radians on a Plane Angle"""
    if isinstance(deg, int):
        return float(deg) * (PI / 180.0)
    elif isinstance(deg, float):
        return deg * (PI / 180.0)
    else:
        raise TypeError
def radian_to_degree(rad):
    """Convert Radians to Degrees Decimal on a Plane Angle."""
    if isinstance(rad, int):
        return float(rad) * (180.0 * PI)
    elif isinstance(rad, float):
        return rad * (180.0 * PI)
    else:
        raise TypeError
def sine(theta, precision = 20, fp = 10) -> float:
    """Approximate the sin with the taylor polnomial or a set number of terms."""
    theta = float((theta + PI) % (2 * PI)) - PI                         # Normalize theta so that it is found between -pi and pi.
    approx_value = 0                                                    # Final Approximation of sin
    neggative = 1                                                       # neggative: 1 = Positive, -1 = Negative
    expnt = 1                                                           # Sum of all odd indexes in the taylor series.

    for _ in range(precision):
        approx_value += (power(theta,expnt) / factorial(expnt)) * neggative     # sin(x) = x - (x^3/3!) + (x^5/5!) - (x^7/7!) ... + (x^n/n!) 
        neggative *= -1
        expnt += 2
    return float(format(approx_value, f'.{fp}f'))
def cossine(theta, precision = 20, fp = 10):
    """Approximate the cos(x)"""
    return sine(theta + (PI/2), precision, fp)
def tangent(theta, precision = 20, fp = 10):
    """Approximate the sin(x)"""
    return sine(theta, precision, fp) / cossine(theta, precision, fp)

def fraction_arctan(theta, precision):
    """ Returns the aproxiamtion or the convergence of Arctan
    using a genralized continued fraction algorithm."""
    theta_sqr = power(theta,2)
    denominator = precision * 2 + 1
    for depth in range(precision, 0, -1):                   # Loop backwards 
        f = depth * 2 - 1
        print(f)
        denominator = f + depth*depth*theta_sqr/denominator
    return theta / denominator

def arctan(theta, precision = 30):
    if theta > 1.0:
        return PI/2.0 - fraction_arctan(1/theta, precision)
    else:
        return fraction_arctan(theta, precision)

print(arctan(1))
   








