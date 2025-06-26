import pytest

# ____________________________________________________________________
# If we want to use fixture in our class then use @pytest.maek.usefixture("fixture method name here")(inbulit Method)
# pass the argument named as scope="class" of the fixture in the conftest file -- so fixture condition execute only once before the class and yield method after the class once

@pytest.mark.usefixtures("setup")
class TestFixtureDemo:

    def test_fixtureDemo1(self):
        print("i'll execute steps in fixtureDemo Method")

    def test_fixtureDemo2(self):
        print("i'll execute steps in fixtureDemo Method")

    def test_fixtureDemo3(self):
        print("i'll execute steps in fixtureDemo Method")

    def test_fixtureDemo4(self):
        print("i'll execute steps in fixtureDemo Method")