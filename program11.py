
import csv

def read_csv_to_dict(filename):
	data = {}
	try:
		with open (filename, 'r', newline = '', encoding='utf-8') as file:
			reader = csv.DictReader(file)
		for row in reader:
			for column, value in row.items():
				if column not in data:
					data[column] = []
				try:
					data[column].append(float(value))
				except ValueError:
					data[column].append(value)
		return data
	except FileNotFoundError:
		print("File not Found!")
		return None
def Summarize_column(data, column, operation):
	if column not in data:
		return "Column not found"

	numeric_values = [v for v in data[column] if instance(v, (int, float))]

	if not numeric_values:
		return "Selected column is not numeric"

	operation = operation.upper()
	if operation == "MAX":
		return max(numeric_values)
	elif operation == "MIN":
		return min(numeric_values)
	elif operation == "AVG":
		return sum(numeric_values) / len(numeric_values)
	else:
		return "Invalid operation"

def main():
	print("Data summary generator")
	filename = input(".student.csv")
