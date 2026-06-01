
#Sorting a text file

f = open("input.txt", "r")
lines = f.readlines()
f.close()

words = []

for line in lines:
	line = line.strip()
	temp = line.split()
	for w in temp:
		words.append(w)

words.sort()
print("No. of lines: ", len(lines))

out = open("output.txt", "w")
for w in words:
	out.write(w + "\n")

print("No. of words in output file: ", len(words))
out.close()
