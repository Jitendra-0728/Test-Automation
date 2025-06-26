# If-Else Condition
greeting = "Good morning!"

if greeting == "Good morning!":
    print("Condition Matches!")
    print("Second Line!")
else :
    print("Condition does not match!")

# -------------------------------------------------------------------------
# For Loop
objects = [1,2,3,4,5,6,7,8,9,10]
for i in objects:
    print(i)            #to print an values of i

# ____________________________________________________________________

# multiplication with the result
for i in objects:       #Result -- 2,4,6,8,10...
    print(i*2)

# ____________________________________________________________________

#Print All Natural Numbers
for i in range(1,15):
    print("Natural Number:" , i)

# ____________________________________________________________________

#Sum
summation = 0
for i in range(1,6):
    summation = summation + i
print(summation)

# ____________________________________________________________________

#Jump the index by specific interval
for i in range(1,15,2):
    print(i)                #Result -- 1,3,5,7,9,11,13

# ____________________________________________________________________

# Skipping first Index / without mentioning start value
for i in range(5):
    print(i)                #Result -- 0,1,2,3,4
