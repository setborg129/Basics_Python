class Complex:
    def __init__(self, real, num=0):
        self.__comple = complex(real, num)

    def __add__(self, other):
        if isinstance(other, Complex):
            other = other.__comple

        complex_ = self.__comple + other
        return Complex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, Complex):
            other = other.__comple
        comple_ = self.__comple * other
        return Complex(comple_.real, int(comple_.imag))

    def __str__(self):
        return self.__comple.__str__()


if __name__ == '__main__':
    c1 = Complex(3, -7)
    c2 = Complex(8)

    print(c1 + c2, complex(3, -4) + complex(4))
    print(c1 * c2, complex(3, -5) * complex(4))
