import os

def list_files_recursive(path):
	for entry in os.listdir(path):
		full_path = os.path.join(path, entry)
		
		if os.path.isdir(full_path):
			print("Folder: ", full_path)
		else:
			file_name = os.path.basename(full_path)
			file_type = os.path.splitext(file_name)
			print("File: ", file_name)
			print("Type: ", file_type)
			print("Path: ", full_path)
			print()

directory_path = './dummy_dir'

list_files_recursive(directory_path)
