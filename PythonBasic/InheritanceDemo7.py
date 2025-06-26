# if parent class have constructor then child class should have constructor

from OOPSDemo6 import Calculator

class ChildClass(Calculator):
    number2 = 200

    def __init__(self):         # its our child constructor so we mandatory have to call parent constructor
        Calculator.__init__(self,2, 10 )    # Parent constructor and parameter(in parent class parameter required for summation so we have to give parameter anyhow while we call Summation method or not)

    def getCompleteDAta(self):
        return self.number1 + self.number2  + self.Summation() #-- 2,10 used when summation method called

inh = ChildClass()
print(inh.getCompleteDAta())