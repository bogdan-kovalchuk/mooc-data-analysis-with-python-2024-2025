#!/usr/bin/env python3

import math


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            base = int(input("Give base of the triangle: "))
            height = int(input("Give height of the triangle: "))
            print(f"The area is {0.5*base*height:1.6f}")
        elif shape == "rectangle":
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            print(f"The area is {width*height:1.6f}")
        elif shape == "circle":
            radius = int(input("Give radius of the circle:"))
            print(f"The area is {math.pi*radius*radius:1.6f}")
        elif shape == "":
            break
        else:
            print("Unknown shape!")
            continue


if __name__ == "__main__":
    main()
