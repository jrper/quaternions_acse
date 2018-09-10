"""Implements a quaternion in python."""

import numpy

class Quaternion(object):

    def __init__(self, x=0, *args):
        self.real = x.real
        self.imag = x.imag
        self.imag2 = getattr(x, 'imag2', 0)
        self.imag3 = getattr(x, 'imag3', 0)
        if args:
            self.imag = args[0]
            self.imag2 = args[1]
            self.imag3 = args[2]

    def __add__(self, x):
        y = Quaternion(self)
        y += x
        return y

    def __radd__(self, x):
        y = Quaternion(x)
        y += self
        return y

    def __iadd__(self, x):
        self.real += x.real
        self.imag += x.imag
        self.imag2 += getattr(x, 'imag2', 0)
        self.imag3 += getattr(x, 'imag3', 0)

        return self    

    def __mul__(self, x):
        y = Quaternion(self)
        y *= x
        return y

    def __rmul__(self, x):
        y = Quaternion(x)
        y *= self
        return y

    def __imul__(self, x):
        a = numpy.array((self.real, self.imag, self.imag2, self.imag3))
        b = numpy.array((x.real, x.imag, 
                         getattr(x, 'imag2', 0), getattr(x, 'imag3', 0)))
        self.real = a[0]*b[0]-numpy.dot(a[1:],b[1:])
        self.imag, self.imag2, self.imag3 = (a[0]*b[1:]+b[0]*a[1:]
                                             +numpy.cross(a[1:],b[1:]))
        return self

    def __sub__(self, x):
        y = Quaternion(self)
        y -= x

        return y

    def __rsub__(self, x):
        y = -Quaternion(x)
        y += x

        return y

    def __isub__(self, x):
        self.real -= x.real
        self.imag -= x.imag
        self.imag2 -= getattr(x, 'imag2', 0)
        self.imag3 -= getattr(x, 'imag3', 0)

        return self

    def __pos__(self):
        return Quaternion(self)

    def __neg__(self):
        return Quaternion(-self.real, -self.imag,
                           -getattr(self, 'imag2', 0),
                           -getattr(self, 'imag3', 0))

    def __repr__(self):
        return "Quaternion(%s, %s, %s, %s)"%(self.real, self.imag,
                                              self.imag2, self.imag3)
    
    def __str__(self):
        return "%s+%si+%sj+%sk"%(self.real, self.imag,
                                self.imag2, self.imag3)

    def conjugate(self):
        return Quaternion(self.real, -self.imag, -self.imag2, -self.imag3)

    def __abs__(self):
        return numpy.sqrt(self.real**2+self.imag**2+self.imag2+self.imag3**2)


i = Quaternion(0,1,0,0)
j = Quaternion(0,0,1,0)
k = Quaternion(0,0,0,1)
