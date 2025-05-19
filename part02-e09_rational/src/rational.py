#!/usr/bin/env python3


class Rational(object):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __add__(self, another):
        return Rational(self.a * another.b + self.b * another.a, self.b * another.b)

    def __sub__(self, another):
        return Rational(self.a * another.b - self.b * another.a, self.b * another.b)

    def __mul__(self, another):
        return Rational(self.a * another.a, self.b * another.b)

    def __truediv__(self, another):
        return Rational(self.a * another.b, self.b * another.a)

    def __eq__(self, another):
        return self.a * another.b == self.b * another.a

    def __gt__(self, another):
        return self.a * another.b > self.b * another.a

    def __lt__(self, another):
        return self.a * another.b < self.b * another.a

    def __str__(self):
        return f"{self.a}/{self.b}"


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
