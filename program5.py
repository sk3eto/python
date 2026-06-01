
import operator
fname = input("Enter the file name: ")

try:
	fhand = open(fname)
	counts = dict()
	for line in fhand:
		words = line.split()
		for word in words:
			if word in counts:
				counts[word] += 1
			else:
				counts[word] = 1
	counts = sorted(counts.items(), key = operator.itemgetter(1), reverse = True)

	for i in range(10):
		print(counts[i])

except:
	print("File cannot be opened!")
