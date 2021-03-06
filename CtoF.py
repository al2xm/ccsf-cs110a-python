# This program produces simple output
# Inputs: none
# Outputs: celsius to fahrenheit
# Written by: C. Conner
# Modified by: Alexander Ma
# Modified Date: Sep 18 2021
print("Celsius Fahrenheit")
print("--------------------")
for celsius in range(-20, 20, 2):
    print(format(celsius, '3.0f'), "\t", format(9 / 5 * celsius + 32, '.1f'))
print("-------------------")