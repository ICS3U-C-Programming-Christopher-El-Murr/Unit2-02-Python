#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 09 26, 2025
# This program is a basic math calculator capable of calculating the circumference of a circle
import constants


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
