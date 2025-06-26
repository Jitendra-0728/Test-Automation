import pytest

from PytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestfixtureDataDemo4:

    def test_editProfile(self, dataLoad):           # dataload as argument --- if want data from the specific test pass the argument and if we want receive any data from that fixture then dont pass as argument
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])

# ____________________________________________________________________
# Same code Execute - Using Logger - Inherit Baseclass --- BaseClass.py

@pytest.mark.usefixtures("dataLoad")
class TestfixtureDataDemo4_1(BaseClass):

    def test_editProfile1(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[0])
        print(dataLoad[2])

