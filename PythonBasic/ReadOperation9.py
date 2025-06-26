
file = open("testFile.txt")

# print(file.read())          # Read Complete Data
# print(file.read(7))         # Read till X number of character or byte
# print(file.readline())       # Read Single line only

# ____________________________________________________________________

# Line by line data using readline method
# Using While loop
# line=file.readline()
# while line!="":
#     print(line)
#     line=file.readline()

# ____________________________________________________________________

# Line by line data using readlines method - treated as list -- easy to alterate and extract data from the list

# for line in file.readlines():       # readline -- each and every line stored in a list
#     print(line)

file.close()