import quaternion.core as qapi
from math import acos

__all__ = [
    'is_unit_quaternion', 'equal_orientation',
    'add', 'sub', 'mul', 'div',
    'conjugate', 'inverse', 'magnitude', 'norm',
    'inner_product', 'delta', 'distance',
]

def is_unit_quaternion(q, tolerance=0.0):
    error = q.magnitude - 1.0

    return error <= tolerance

def are_identical(q, p, tolerance=0.0):
    error = q - p

    if q.a > tolerance:
        return False

    if q.b > tolerance:
        return False

    if q.c > tolerance:
        return False

    if q.d > tolerance:
        return False

    return True

def equal_orientation(q, p, tolerance=0.0):
    theta = angle_of_separation(q, p)

    return theta <= tolerance

def add(q, p):
    return q + p

def sub(q, p):
    return q - p

def mul(q, p):
    return q * p

def scale(q, s):
    return s * q

def div(q, p):
    return q / p

def conjugate(q):
    return q.conjugate

def inverse(q):
    return q.inverse

def magnitude(q):
    return q.magnitude

def norm(q):
    return q.norm

def inner_product(q, p):
    a = q.a * p.a
    b = q.b * p.b
    c = q.c * p.c
    d = q.d * p.d

    return a + b + c + d

def angle_of_separation(q, p):
    return acos(2 * inner_product(q, p) ** 2 - 1)

def distance(q, p):
    return 1 - inner_product(q, p)

def delta(q, p):
    return q * p.inverse
