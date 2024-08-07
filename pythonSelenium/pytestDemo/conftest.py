import pytest


@pytest.fixture(scope="class")
def setup():
    print("code here will get executed before test case")
    yield
    print("code here will get executed after test case gets executed")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "Mudasir"), ("Firefox", "Ahmed"), ("IE", "empty")])
def crossBrowser(request):
    return request.param
