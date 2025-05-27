#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range [tmin,tmax]."""
    a_min = np.min(a)
    a_max = np.max(a)
    if a_min == a_max:
        return np.zeros_like(a, dtype=float)
    return (a - a_min) / (a_max - a_min) * (tmax - tmin) + tmin


def center(a):
    h, w = a.shape[:2]
    return (h - 1) / 2, (w - 1) / 2


def radial_distance(a):
    y_idx, x_idx = np.indices(a.shape[:2])
    center_y, center_x = center(a)
    return np.sqrt((y_idx - center_y) ** 2 + (x_idx - center_x) ** 2)


def radial_mask(a):
    dist = radial_distance(a)
    dist_scaled = scale(dist)
    return 1.0 - dist_scaled


def radial_fade(a):
    return a * radial_mask(a)[:, :, np.newaxis]


def main():
    painting = plt.imread("src/painting.png")

    print(center(painting))
    print(radial_distance(painting))

    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(painting)
    ax[1].imshow(radial_mask(painting))
    ax[2].imshow(radial_fade(painting))
    plt.show()


if __name__ == "__main__":
    main()
