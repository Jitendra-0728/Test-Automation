# Classes - user defined blueprint
# Sum, Multiplication, Addition, Constant
# have - methods, class variable, instance variable, constructor etc
# objects for your classes
# functions when we used into the class that called as a Method
# Constructor is a method which is automatically called when we create object for any class
# Self keyword is mandatory for calling variable names into method
# Instance variables are attached to the object (instance) of a class
# Class variables are attached to the class itself (not to the object) and shared among all instances.
# Constructor name should be __init__

class Calculator:
    number1 = 100       # Class Variable (numbers) - variable which are immediately inside the class

    def __init__(self, a,b):
        self.firstNumber = a        # Instance Variable (self.firstNumber)- variable which are declared inside the constructor  - keep changing on every object creation
        self.secondNumber = b
        print("Parent Constructor")

    def getData(self):
        print("First Method")

    def getData2(self):
        print("Second Method")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.number1

cal=Calculator(2,3)    # Object Creation
print(cal.number1)  # Variable Access
cal.getData()       # Method Access
cal.getData2()
print(cal.Summation())
