#  File: shapes.py
#  This program contains a user-defined functions for calculations related to
#  shapes stadium and rhombus
#  test code is found in in main()
#  Written by: C. Conner
#  Modified by: Alexander Ma
#  Modified Date: 10/01/2021


import math


# RHOMBUS FUNCTIONS HERE #
#def rhombus_area(length_a, length_b):
        #return (length_a * length_b) / 2


#def rhombus_perimeter(length):
        #return 4 * length


# STADIUM FUNCTIONS HERE #
def stadium_area(radius, length):
        return ((math.pi) * (radius) ** 2) + (2 * radius * length)


def stadium_perimeter(radius, length):
        return 2 * (math.pi * radius + length)


# TEST
def main():
        #diagonal test data for rhombus
        length_a = 20
        length_b = 10

        #test data for all shapes
        length = 50
        width = 25
        radius = 15

        #TEST rhomobus functions

        #print("rhombus area with", length_a, length_b, "==", 100.0)
        #print("Test Result: ", rhombus_area(length_a, length_b))

        #print("rhombus perimeter args", length, "==", 200)
        #print("Test Result:", rhombus_perimeter(length))

        # TEST stadium functions

        print("stadium area with", radius, length, "==", 2206.858347057703)
        print("Test Result:", stadium_area(radius, length))

        print("stadium perimeter args", radius, length, "==", 194.2477796076938)
        print("Test Result: ", stadium_perimeter(radius, length))
main()