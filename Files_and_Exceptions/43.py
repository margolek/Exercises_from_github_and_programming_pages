"""
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by reading
in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.

"""
#-----Sample of absolute path-----#

#filename = r'C:\Users\margo\OneDrive\Pulpit\example.txt'

#with open(filename) as file_object:
#	contents = file_object.read()
#	print(contents.rstrip())


filename = r'learning_python.txt'


#-----Reading entire file-----#
with open(filename) as file_object:
	contents = file_object.read()
	print(contents)

print()

#-----Looping over the file object-----#
with open(filename) as file_obejct1:
	for line in file_obejct1:
		print(line.rstrip())

print()

#-----Storing line in a list-----#
with open(filename) as file_object2:
	lines = file_object2.readlines()

print(lines)

for line in lines:
	print(line.rstrip())	