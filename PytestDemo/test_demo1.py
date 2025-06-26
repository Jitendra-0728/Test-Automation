import pytest

@pytest.mark.smoke                  #to run statement in cmd use command like --- py.test -m smoke(GivemName) -v -s
def test_firstProgram(setup):       # def -- function declaration, test_( Method Name ) -- test method name
    print("         Hello World")


@pytest.mark.xfail                  # statements get execute but dont show the report like PASS / FAIL
def test_secondProgram():
    print("         Good Morning")

# ____________________________________________________________________
# Parameterization - fixture in conftest file

def test_corssBrowser(crossBrowser):
    # print(crossBrowser)
    print(crossBrowser[1])
    # print(crossBrowser[1])




