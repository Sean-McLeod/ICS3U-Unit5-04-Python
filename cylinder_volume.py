#!/usr/bin/env python3

# Created by Sean McLeod
# Created on January 2021
# This program calculates the volume of a cylinder

import math


def cylinder_volume(radius, height):
    # this function calculates the volume of a cylinder

    # process
    volume = math.pi*radius**2*height

    return volume


def main():
    # this function gets radius and height

    print("This program calculates the volume of a cylinder")
    print("\n")

    # input
    user_radius = input("Enter in a radius(mm): ")
    user_height = input("Enter in a height(mm): ")
    print("\n")

    try:
        int_user_radius = int(user_radius)
        int_user_height = int(user_height)

        if int_user_radius > 0 and int_user_height > 0:
            # call functions
            final_cylinder_volume = cylinder_volume(int_user_radius,
                                                    int_user_height)

            # output
            print("The volume is {}mm²".format(final_cylinder_volume))

        else:
            print("The values should be positive")

    except Exception:
        print("This is an invalid number")


if __name__ == "__main__":
    main()
