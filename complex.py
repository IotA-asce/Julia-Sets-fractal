"""
complex number
"""

import math

class Complex:
    """
    Complex class for representing and performing operations related to complex numbers.

    This class allows the creation of complex numbers, 
    as well as performing arithmetic operations with them.

    Attributes:
    real (float): The real component of the complex number.
    imag (float): The imaginary component of the complex number.

    Methods:
    add (self, other): Adds two complex numbers.
    sub (self, other): Subtracts two complex numbers.
    mul (self, other): Multiplies two complex numbers.
    truediv (self, other): Divides two complex numbers.
    abs (self): Returns the magnitude of the complex number.
    str (self): Returns a string representation of the complex number in the form 'real + imagj'.
    """

    def __init__(self, _re=None, _im=None, _mag=None, _angle=None) -> None:
        if _mag is not None and _angle is not None:
            self._re = _mag * math.cos(_angle)      # real part
            self._im = _mag * math.sin(_angle)      # complex part
        else:
            self._re = _re
            self._im = _im

    def __repr__(self) -> str:
        return f"{self._re} + {self._im}i"

    def __add__(self, other):
        _re = self._re + other._re
        _im = self._im + other._re

        return Complex(_re=_re, _im=_im)

    def __sub__(self, other):
        _re = self._re - other._re
        _im = self._im - other._im

        return Complex(_re=_re, _im=_im)

    def __mul__(self, other):
        _a, _b = self._re, other._re
        _c, _d = self._im, other._im

        _re = _a * _c - _b * _d
        _im = _a * _d + _b * _c
        
        return Complex(_re=_re, _im=_im)


    def __truediv__(self, other):
        _a, _b = self._re, self._im
        _c, _d = other._re, other._im

        _re = (_a*_c + _b*_d) / (_c**2 + _d**2)
        _im = (_b*_c - _a*_d) / (_c**2 + _d**2)

        return Complex(_re=_re, _im=_im)

    def set(self, _re=None, _im=None, _mag=None, _angle=None):
        """
        undocumented
        """
        if _mag is not None and _angle is not None:
            self._re = _mag * math.cos(_angle)      # real part
            self._im = _mag * math.sin(_angle)      # complex part
        else:
            self._re = _re
            self._im = _im

    def magnitude(self):
        """
        Return the modulus (magnitude) of a complex number.

        The modulus of a complex number is calculated as the square root of the sum of
        the squares of its real and imaginary parts.

        Returns:
        float: The modulus of the input complex number.
        """

        return math.sqrt(self._re**2 + self._im**2)

    def angle(self):
        """
        Returns the argument of the complex number

        The argument of a complex number is the angle that the number
        makes with the positive real axis

        Returns:
        float(radians): the argument of the complex number
        """

        return math.atan2(self._im, self._re)

    def conjugate(self):
        """
        Return the conjugate of a complex number.

        The conjugate of a complex number is calculated by multiplying its imaginary part
        by -1 and keeping its real part unchanged.

        Returns:
        Complex: The conjugate of the input complex number.
        """

        return Complex(_re=self._re, _im=self._im * -1)

    def polar(self):
        """
        Return the polar representation of a complex number.

        The polar representation of a complex number consists of its magnitude (modulus) and
        angle (argument).

        Returns:
        tuple: A tuple containing the magnitude and angle of the input complex number.
        """

        return self.magnitude(), self.angle()

    def exponential(self, _n):
        """
        Return the n-th power of a complex number in exponential form.

        The n-th power of a complex number in exponential form is calculated by raising its
        magnitude to the power of n and multiplying its angle by n.

        Args:
        n (int): The power to raise the complex number to.

        Returns:
        Complex: The n-th power of the input complex number in exponential form.
        """

        _mag = self.magnitude() ** _n
        _angle = self.angle() * _n

        return Complex(_mag=_mag, _angle=_angle)
