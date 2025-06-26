# --QUE--   Reverse the data from the file and store

# read the file and store all the lin in list
# reverse the list
# write the list back to the file

# Step - 1
# file = open("testFile.txt")
# data = file.readlines()
# file.close()
# reversed(data)

# file = open("testFile.txt", "w")
# for line in reversed(data):
#     file.write(line)
# file.close()

# ____________________________________________________________________

# Step-2
# using this way we don't need to write file.close()
with open("testFile.txt", "r") as Reader:
    data = Reader.readlines()
    reversed(data)
    with open("testFile.txt", "w") as Writer:
        for line in reversed(data):
            Writer.write(line)