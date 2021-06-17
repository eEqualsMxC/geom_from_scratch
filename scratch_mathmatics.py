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
    return x ** n
    

a = sqr_root(49)
print(a)





