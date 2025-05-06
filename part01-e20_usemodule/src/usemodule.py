#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    print(triangle.hypotenuse(5, 10))
    print(triangle.area(5, 10))


if __name__ == "__main__":
    main()
