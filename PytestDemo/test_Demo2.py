import pytest


@pytest.mark.smoke                  #to run statement in cmd use command like --- py.test -m smoke(GivemName) -v -s
@pytest.mark.skip
def test_firstProgram():
    message= "Hello World"
    assert message == "Hi", "Message doesnot match"


def test_secondProgramCreditCard(setup): #to run statement in cmd use command like ---py.test -k creditcard(any string name from testmethod) -v -s
    a = 4
    b = 5
    assert a+1 == 5, "Addistion doesnot match"

