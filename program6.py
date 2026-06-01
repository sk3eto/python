
#Reading the marks of 6 subjects

marks = []

for i in range(6):
	m = float(input(f"Enter the marks of subject {i + 1}: "))
	marks.append(m)

print(marks)

n = len(marks)

for i in range(n):
	for j in range(0, n - i - 1):
		if marks[j] < marks[j + 1]:
			marks[j], marks[j + 1]  = marks[j + 1], marks[j]

print("Marks from High to loww using Bubble sort technique is: ")
for m in marks:
	print(m)
