#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(image):
    painting = image.copy()
    r = painting[:, :, 0]
    g = painting[:, :, 1]
    b = painting[:, :, 2]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def to_red(image):
    painting = image.copy()
    painting = image.copy()
    painting[:, :, 1] = 0
    painting[:, :, 2] = 0
    return painting


def to_green(image):
    painting = image.copy()
    painting[:, :, 0] = 0
    painting[:, :, 2] = 0
    return painting


def to_blue(image):
    painting = image.copy()
    painting[:, :, 0] = 0
    painting[:, :, 1] = 0
    return painting


def main():
    painting = plt.imread("src/painting.png")
    grayscale_painting = to_grayscale(painting)
    plt.imshow(grayscale_painting)
    plt.show()

    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(painting))
    ax[1].imshow(to_green(painting))
    ax[2].imshow(to_blue(painting))
    plt.show()


if __name__ == "__main__":
    main()
