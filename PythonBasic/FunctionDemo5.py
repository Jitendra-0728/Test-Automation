# Function is a group of related statement that perform a specific task
# def -- keyword / Identifier used to create function

# ____________________________________________________________________

def GreetMe():      # Function Declaration
    print("Function")
GreetMe()   # Function Calling

# ____________________________________________________________________

# 1 -Parametarized Function
def GreetMe(name):
    print("Hello " + name)
GreetMe("Deadshadow")

# ____________________________________________________________________

# 2 -
def AddInteger(a,b):
    print("Sum is : ", a+b)         #return a+b
AddInteger(10,20)            #print(AddInteger(10,20))
