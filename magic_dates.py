# The date June 10, 1960, is special because when it is written in the following
# format, the month times the day equals the year:
# Inputs:  month, a day, and a two digit year
# Outputs:  if year is magic
# Written by: C. Conner
# Modified by:  Alexander Ma
# Modified Date: 09/11/2021
userMonth = int(input("please enter a month: "))
userDay = int(input("please enter a day: "))
userYear = int(input("please enter a two digit year: "))

if userMonth * userDay == userYear:
    print("The date is magic")
else:
    print("The date is not magic")
