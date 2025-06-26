
from Tools.scripts.make_ctype import values

# ____________________________________________________________________

# List      --  Mutable(can change / update)  allows multiple data types that allows multiple values and can be different data types
list = [1,2,"hello", 5,6,7]
print(list[2])    #result -- hello
print(list[-1])   #result -- 7
print(list[1:4])  #result -- 2, hello,5   -- 4 means -1 so result is 5 not the 6
print(list[0])    # result -- 1
print(list)

# ____________________________________________________________________

# insert
list.insert(6, "Six")         #result -- [1, 2, 'hello', 5, 6, 7, 'Six']
print(list)
list.append("end")    #to update last value # [1, 2, 'hello', 5, 6, 7, 'Six', 'end']
print(list)

# ____________________________________________________________________

#Update
list[2] = "HELLO"         #result -- [1, 2, 'HELLO', 5, 6, 7, 'Six', 'end']
print(list)

# ____________________________________________________________________

#Delete
del list[0]
print(list)           #result -- [2, 'HELLO', 5, 6, 7, 'Six', 'end']

# ____________________________________________________________________

# Tuple      --  Immutable(can not  change / update)  allows multiple data types that allows multiple values and can be different data types
tuple = (1, 2, 3.1, "Tuple")
print(tuple)

# ____________________________________________________________________

# Dictionary      --
dictionary = {"one":1, 2:"two","three":"third pair"}
print(dictionary)

print(dictionary[2])        # provide key not index number
print(dictionary["three"])

dictionary[4] = "Four"
print(dictionary)

# create dictionary dynamic -- runtime
dict = {}
dict["Runtime"] = "Dynamically"     # created dynamically
dict["Runtime"] = "Dynamically_"    # Update
dict["FirstName"] = "Jitendra"
print(dict["FirstName"])
print(dict)