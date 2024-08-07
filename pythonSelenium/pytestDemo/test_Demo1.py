# all pytestDemo files should start with test_
# pytestDemo method names should start with test_
# any code should be wrapped in method
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
