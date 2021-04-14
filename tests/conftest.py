import pytest
import requests
from tests.consts_and_variables import *
import datetime as DT
from datetime import datetime
from funcs.birthday_list_api_helper import *
import os.path
import calendar

"""
Данный файл содержит фисктуры доступные для тестов
"""


def pytest_addoption(parser):
    parser.addoption("--basic_url", action="store", default="http://129.146.247.102:5000/")
    parser.addoption("--hello_url", action="store", default="http://129.146.247.102:5000/hello/")
    parser.addoption("--users_url", action="store", default="http://129.146.247.102:5000/users")


@pytest.fixture()
def year_ago_date():
    date = datetime.date(datetime.now())
    date = date.replace(year=date.year - 1)
    return date.strftime("%Y-%m-%d")


@pytest.fixture()
def current_year():
    date = datetime.date(datetime.now())
    return int(date.strftime("%Y"))


@pytest.fixture()
def almost_year_ago():
    return datetime.date(datetime.now()) - DT.timedelta(days=360)


@pytest.fixture()
def remove_default_user():
    requests.delete(hello_requests_url + default_username)


@pytest.fixture()
def create_new_user_year_ago(year_ago_date):
    requests.post(hello_requests_url + default_username, json={"dateOfBirth": year_ago_date})


@pytest.fixture()
def create_new_user_almost_year_ago(almost_year_ago):
    requests.post(hello_requests_url + default_username, json={"dateOfBirth": almost_year_ago.strftime("%Y-%m-%d")})


@pytest.fixture(scope="function")
def get_default_user_response():
    return requests.get(hello_requests_url + default_username)


@pytest.fixture()
def create_default_user():
    requests.post(hello_requests_url + default_username, json={"dateOfBirth": default_birthdate})


@pytest.fixture()
def create_default_user_response():
    return requests.post(hello_requests_url + default_username, json={"dateOfBirth": default_birthdate})


@pytest.fixture()
def create_default_2012_user_response():
    return requests.post(hello_requests_url + default_username, json={"dateOfBirth": default_birthdate_2012})


@pytest.fixture()
def remove_default_user_response():
    return requests.delete(hello_requests_url + default_username)


@pytest.fixture()
def get_users_list_response():
    return requests.get(users_list_url)


@pytest.fixture()
def put_default_user_response():
    return requests.put(hello_requests_url + default_username, json={'dateOfBirth': default_birthdate})


@pytest.fixture()
def put_default_2012_user_response():
    return requests.put(hello_requests_url + default_username, json={'dateOfBirth': default_birthdate_2012})


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            f.write(rep.longreprtext + "\n")
