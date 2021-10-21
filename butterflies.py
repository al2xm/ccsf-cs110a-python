# This program calculates butterfly population estimates
# Inputs:  males, estimated number of male butterflies
#          females, estimated number of female butterflies
# Outputs: total butterflies, sex ratio, variance
#          gender difference, mating pairs
# Written by: C. Conner
# Modified by:  Alexander Ma
# Modified Date: Use format 09/06/2021 (example: 09/10/2021)

print("Butterfly Estimator\n")
print("Enter the estimated males population: ")
# input/get data
males = int(input("Enter the estimated males population: "))
females = int(input("Enter the estimated females population: "))

# perform calculations
total_butterflies = males + females
sex_ratio = males // females
ratio_variance = males % females
gender_difference = males - females
mating_pairs = males * females

# output results
print("\nTotal Butterflies: " , total_butterflies)
print("Sex Ratio          : " , sex_ratio)
print("Variance           : " , ratio_variance)
print("Gender Difference          : " , gender_difference)
print("Mating Pairs          : " , mating_pairs)