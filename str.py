with open('example.txt', 'r') as in_file:
	print in_file.read().split("\\n")[2].split("at")[0]
	
raw_input()