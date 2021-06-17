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
def sine(theta, pp = 20, fp = 10) -> float:
    """Approximate the sin with the taylor polnomial or a set number of terms."""
    theta = float((theta + PI) % (2 * PI)) - PI                         # Normalize theta so that it is found between -pi and pi.
    approx_value = 0                                                    # Final Approximation of sin
    neggative = 1                                                       # neggative: 1 = Positive, -1 = Negative
    expnt = 1                                                           # Sum of all odd indexes in the taylor series.

    for _ in range(pp):
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

# class Circle(Trig):
#     """A class for a circle on a cartesian plane"""
#     def __init__(self, radius: float = None) -> Circle:
#         super(Circle, self).__init__()
#         self.radius = radius

    
    

"""Return a factorial of an integer."""
fact = lambda x: 1 if x == 0 else x * factorial(x - 1)


# def sin(theta: float, )

# print(PI)
# import math
# from point import Point
# p1 = Point(1,2) 
# p2 = Point(2,3)
# p3 = Point(3,4)

# def rise(pt1, pt2) -> float:
#     return pt2.y - pt1.y

# def run(pt1, pt2) -> float:
#     return pt2.y - pt1.y

# def slope(pt1, pt2):
#     return rise(pt1,pt2) / run(pt1,pt2)


# ad_1 = run(p1, p2)
# op_1 = rise(p1, p2)
# h_1 = p1.distance(p2)


# # temp_pt = Point(p1.x + run, p1.y)

# dis = p2.distance(p3) # This will be given

# h_2 = h_1 + dis 
# sin_theta = op_1 / h_1
# op_2 =  sin_theta * h_2
# y_coor =  p1.y + op_2
# ad_2 = ((h_2) ** 2 -(op_2) ** 2) ** 0.5
# x_coor = p1.x + ad_2
# fp = Point(x_coor,y_coor)
# tp = Point(3,4)


# print(op_2/h_2)         






# slp = slope(p1, p3)






