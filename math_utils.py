import math

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative number not allowed")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def area_of_circle(radius: float) -> float:
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * radius * radius
