from sys import argv

script, input_file = argv

def rewind(f):
	f.seek(22)
	print f.readline()
	
def print_all(f):
	print f.read(),

def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print_all(current_file)


current_line = 12
print_a_line(current_line, current_file)

current_line += 1

rewind(current_file)

print_a_line(current_line, current_file)

current_file.close()