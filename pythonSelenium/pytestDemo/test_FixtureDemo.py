import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("fixtureDemo: code here gets executed after setup()")

    def test_fixtureDemo1(self):
        print("fixtureDemo1: code here gets executed after setup()")

    def test_fixtureDemo2(self):
        print("fixtureDemo2: code here gets executed after setup()")

    def test_fixtureDemo3(self):
        print("fixtureDemo3: code here gets executed after setup()")
