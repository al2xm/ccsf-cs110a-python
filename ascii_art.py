#  File: ascii_art
#  This program contains a list of code that opens,
#  writes, and reads/readlines, and closes code
#  test code is found in in main()
#  Written by: C. Conner
#  Modified by: Alexander Ma
#  Modified Date: 10/06/2021


print('HERE IS MY CONSOLE OUTPUT\n')

file = open('ascii_art.txt', 'w')
file.write('Torpedo in water\n')
file.write("~^~^~'====>`~^~^~^~^~\n")
file.write('Creates fish bones\n')
file.write('>++(''>\n')
file.write('On wave\n')
file.write('_.~"~._.~"~._.~"~._.~"~._\n')

file.close()


file = open('ascii_art.txt', 'r')
for line in file:
    print(line, end='')

print('\nPROGRAM FINISHED')



