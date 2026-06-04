
print("Student info program")
D = []
n = int(input("No. of student records: "))

for _ in range(n):
	fname, lname = input("Enter full name: ").split()
	contact = input("Enter the contact number: ")
	if len(contact) < 10:
		print("Invalid Contact Number!")
		exit()
	marks = int(input("Enter the marks of the student: "))
	data = {
		"First_name": fname,
		"Last_name": lname,
		"Contact": contact,
		"Marks": marks
	}
	D.append(data)
print(D)
def sort_names():
	print("\nSort Names")
	for name in sorted(D.keys()):
		print(name[0], name[1])

def min_marks():
	minimum = min(m for m in D.values())
	print("Minimum marks: ", minimum)

def search_contact(fname):
	found = False
	for(first, last), (contact, marks) in D.items():
		if first == fname or last == lname:
			print("Found record!")
			print("Contact: ", contact)
			found = True
		if not found:
			print("Student not found!")
