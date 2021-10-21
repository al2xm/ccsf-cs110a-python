#  File: dog_names.py
#  This program contains that uses list and tuples,
#  for dog names
#  test code is found in in main()
#  Written by: C. Conner
#  Modified by: Alexander Ma
#  Modified Date: 10/14/2021

def main():
    try:
        file = open("dog_names.txt", "r")
    except IOError:
        print('Error reading from file')
        return

    lines = file.readlines()
    file.close()

    stripped = []
    for line in lines:
        stripped.append(line.rstrip())

    name = input("Enter a dog\'s name to check if it is one of the most popular: ")

    if name in stripped:
        print(name + ' is one of the most popular dog\'s names.')
    else:
        print(name + ' is not one of the most popular dog\'s names.')


if __name__ == "__main__":
    main()
