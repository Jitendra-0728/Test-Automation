from os.path import split

from Tools.scripts.var_access_benchmark import steps_per_trial

str = "RahulShettyAcademy.com"
str1 = "Consulting Firm"
str2 = "RahulShetty"

print(str[0])   # O/P -- R
print(str[1])   # O/P -- a
print(str[0:5]) # O/P -- Rahul  -- if we want SubString

# ____________________________________________________________________

# 1 - Concatenation
string2 = str + " " + str1     # Concate with space -- RahulShettyAcademy.com Consulting Firm
print(string2)

# 2
string2 = str+str1             # Concate WithOut space -- RahulShettyAcademy.comConsulting Firm
print(string2)

# 3
string3 = str2+str1
print("value of str3 is: " , string3)
# ____________________________________________________________________

# 1 - validate string present in another string or not
print(str2 in str)              # Show True or False

# 2 - Using if-else Condition
if "RahulShetty" in str:
    print("Yes, 'RahulShetty' is present in the given string")
else:
    print("No, 'RahulShetty' is not present in the given string")

# ____________________________________________________________________

# Split
spl=str.split(".")
print(spl)
print(spl[0])
print(spl[1])

# ____________________________________________________________________

# Strip - Trim(JAVA) -- To remove white spaces from the string
string4 = "   RahulShettyAcademy.com   "
print(string4.strip())          # Remove complete spaces
print(string4.lstrip())         # Remove Left spaces
print(string4.rstrip())         # Remove Right spaces

