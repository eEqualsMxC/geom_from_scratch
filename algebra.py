from typing import Union

def power(x:int, exp:int) -> int:
    """Caculate x ^ exp"""
    return 1 if exp == 0 else x * pow(x, exp - 1)
def factorial(x: int) -> int:
    """Calculate factorial of integer x """
    if isinstance(x, int):
        return 1 if x == 0 else x * factorial(x - 1)
    else:
        raise ValueError(f"Integer Only")
def sqr_root(x: Union[int, float]) -> float:
    return x ** 0.5 
def nth_root(x, n):
    return x ** (1 / n)
def float_abs(x: Union[float, int]) -> float:
    """Return abs(x)"""
    if isinstance(x, int):
        x = float(x)
    if not isinstance(x, float):
        raise TypeError
    if x < 0:
        x *= -1.0
    return x

def logit(product, base = 10, fp = 4) -> float:

    if base <= 0 or base == 1 or product <= 0:
        return float('nan')
    if base == product:
        return 1
    if product == 1:
        return 0
    expnt = 1
    nearest = False
    while not nearest:
        err = float_abs(product - power(base, expnt))      
        if err > float_abs(product - power(base, expnt + 1)):
            expnt += 1
        elif err > float_abs(product - power(base, expnt - 1)):
            expnt -= 1
        else:
            nearest = True

    iterations = 20
    power_change = 1

    for _ in range(iterations):
        power_change /= 2
        err = float_abs(product - power(base, expnt))
        if err > float_abs(product - power(base, expnt + power_change)):
            expnt += power_change
        elif err > float_abs(product - power(base, expnt - power_change)):
            expnt -= power_change
    return float(format(expnt, f'.{fp}f'))







