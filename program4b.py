
#Frequency of each digit

n = input("Enter a number: ")

freq = {}

for i in n:
	if i in freq:
		freq[i] += 1
	else:
		freq[i] = 1

print("Count of all character is: ", freq)
