# all pytestDemo files should start with test_
# pytestDemo method names should start with test_
# any code should be wrapped in method
# -s for logs in terminal, -v for more info, -k for method names execution,
# we can run specific .py file by py.test filename
# we can mark test cases with @pytest.mark.customname & run with -m
# we can skip test cases with @pytest.mark.skip
# to skip test case execution status in report, use @pytest.mark.xfail
# fixtures are used for setup & tear down methods for test cases
# conftest file is required as a common file to generalize fixtures for all test cases
# data-driver & parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run before class is initiated & at the end

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "Demo2 failed because strings do not match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a + 2 == b, "Sum does not match"


def test_fixtureDemo(setup):
    print("I'll execute after setup() gets executed")
