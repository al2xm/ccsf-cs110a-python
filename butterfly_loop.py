# This program calculates butterfly caught
# Inputs:  number of butterflies cautch
# Outputs: total butterflies,
# Written by: C. Conner
# Modified by:  Alexander Ma
# Modified Date: 9/21/2021

def butterfly():
    print("WELCOME TO THE BUTTERFLY COLLECTING PROGRAM!\n")
    print("Enter the number of butterflies you have collected.")
    print("Please enter -1 when finished.\n")
    butterflies = int(input("Enter the number of butterflies collected: "))
    total = 0
    while (butterflies != -1):
        total += butterflies
        print(str(butterflies))
        butterflies = int(input("Enter the number of butterflies collected: "))

    print("\nHERE ARE THE RESULTS OF YOUR BUTTERFLY COLLECTED\nTotal bugs collected: " + str(total))
butterfly()

