import importlib
import os
import pytest
from fixture.application import Application
import re


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Users\\Elena\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_excel(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])


def load_from_excel(file):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "$s.xlsx" % file)

