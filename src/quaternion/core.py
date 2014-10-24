class IQuaternion(object):
    def __init__(self, a, b, c, d):
        raise NotImplemented()

    def __mul__(self, other):
        raise NotImplemented()

    def __add__(self, other):
        raise NotImplemented()

    def __sub__(self, other):
        raise NotImplemented()

    def __neg__(self):
        raise NotImplemented()

    @property
    def a(self):
        raise NotImplemented()

    @a.setter
    def a(self, value):
        raise NotImplemented()

    @property
    def b(self):
        raise NotImplemented()

    @b.setter
    def b(self, value):
        raise NotImplemented()

    @property
    def c(self):
        raise NotImplemented()

    @c.setter
    def c(self, value):
        raise NotImplemented()

    @property
    def d(self):
        raise NotImplemented()

    @d.setter
    def d(self, value):
        raise NotImplemented()

    @property
    def magnitude(self):
        raise NotImplemented()

    @property
    def conjugate(self):
        raise NotImplemented()

    @property
    def inverse(self):
        raise NotImplemented()

    @property
    def real(self):
        raise NotImplemented()

    @property
    def imag(self):
        raise NotImplemented()

from math import sqrt

from api import IQuaternion

class BaseQuaternion(IQuaternion):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __neg__(self):
        return self * -1.0

    def __add__(self, other):
        q = self
        p = other

        a = q.a + p.a
        b = q.b + p.b
        c = q.c + p.c
        d = q.d + p.d

        return self.__class__(a, b, c, d)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, int):
            return self._mul_by_scalar(other)

        if isinstance(other, float):
            return self._mul_by_scalar(other)

        raise TypeError()

    def __rmul__(self, other):
        return self.__mul__(other)

    def _mul_by_quaternion(self, quaternion):
        a = self.a
        b = self.b
        c = self.c
        d = self.d

        e = quaternion.a
        f = quaternion.b
        g = quaternion.c
        h = quaternion.d

        a = a * e - b * f - c * g - d * h
        b = b * e + a * f + c * h - d * g
        c = a * g - b * h + c * e + d * f
        d = a * h + b * g - c * f + d * e

        return self.__class__(a, b, c, d)

    def _mul_by_scalar(self, scalar):

        a = self.a * scalar
        b = self.b * scalar
        c = self.c * scalar
        d = self.d * scalar

        return self.__class__(a, b, c, d)

    @classmethod
    def from_quaternion(cls, q):
        return cls(q.a, q.b, q.c, q.d)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = float(value)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = float(value)

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = float(value)

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = float(value)

    @property
    def real(self):
        return self.a

    @property
    def imag(self):
        return complex(self.b), complex(self.c), complex(self.d)

    @property
    def conjugate(self):
        a = self.a
        b = -self.b
        c = -self.c
        d = -self.d

        return self.__class__(a, b, c, d)

    @property
    def magnitude(self):
        return sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2)

class Quaternion(BaseQuaternion):
    def __init__(self, a, b, c, d):
        super(Quaternion, self).__unit__(a, b, c, d)

    def __mul__(self, other):
        if isinstance(other, IQuaternion):
            return self._mul_by_quaternion(other)

        return super(Quaternion, self).__init__(other)

    @property
    def inverse(self):
        self.conjugate / self.magnitude

from api import BaseQuaternion, Quaternion

class UnitQuaternion(BaseQuaternion):
    def __init__(self, a, b, c, d):
        super(UnitQuaternion, self).__init__(a, b, c, d)
        self.a /= self.magnitude
        self.b /= self.magnitude
        self.c /= self.magnitude
        self.d /= self.magnitude

    def __mul__(self, other):
        if isinstance(other, UnitQuaternion):
            return self._mul_by_quaternion(other)

        if isinstance(other, Quaternion):
            other = self.from_quaternion(other)
            return self._mul_by_quaternion(other)

        return super(UnitQuaternion, self).__mul__(other)

    @property
    def inverse(self):
        return self.conjugate
