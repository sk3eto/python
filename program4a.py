
import math

n = int(input("Enter the no. of elements: "))
numbers = []

for i in range(n):
	value = float(input("Enter number: "))
	numbers.append(value)

#Calculating the mean

mean = sum(numbers)/n

#Calculating the variance

variance = 0
for x in numbers:
	variance += (x - mean) ** 2
variance = variance / n

#Calculating the standard deviation

std_dev = math.sqrt(variance)

#Displaying the result

print("Mean: ", mean)
print("Variance: ", variance)
print("Standard Deviation: ", std_dev)

