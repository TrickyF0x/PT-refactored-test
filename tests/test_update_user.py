import pytest
import http
from funcs.birthday_list_api_helper import *
from consts_and_variables import *

"""
Тесты посвященные обновлению данных даты рождения пользователя в БД
Каждый тест соответсвует тест-кейсу из документации
Включает тест-кейсы со 6 по 9
"""


"""
Тест кейс 6 Обновление даты рождения
Позитивный сценарий в котором по заданному имени пользователя должна быть обновлена его дата рождения
"""
def test_basic_user_date_updating(create_default_user, put_default_2012_user_response):
    if user_not_in_base(default_username):
        errors.append("ERROR, user not created")
    if not put_default_2012_user_response.status_code == http.HTTPStatus.NO_CONTENT:
        errors.append(f"Wrong status code, response code is {put_default_2012_user_response.status_code}")
    if not user_exists_changed_and_alone(default_username, default_birthdate_2012):
        errors.append("Error, user doesnt exist or not updated")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))


"""
Тест кейс 7 Добавление пользователя с именем, уже существующем в БД
Сценарий в котором обновляется дата рождения пользователя, которого еще нет в БД т.е. создается новый пользователь
"""
def test_update_not_existing_user(remove_default_user, put_default_user_response):
    if not put_default_user_response.status_code == http.HTTPStatus.CREATED:
        errors.append(f"Wrong status code, response code is {put_default_user_response.status_code}")
    if not correct_user_created(default_username, default_birthdate):
        errors.append("Error, user doesnt exist or not updated")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))


"""
Тест кейс 8 Обновление при некорректном формате даты
Негативный сценарий в котором проверяется создание/обновление пользователя при некорректном формате даты рождения
"""
@pytest.mark.parametrize("args, expected_result", [
    pytest.param(incorrect_birthdate_format, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Incorrect birthdate format to update", ),
    pytest.param(incorrect_birthdate_not_exists, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Not existing date incorrect format to update", ),
    pytest.param(incorrect_birthdate_letters, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Random numerics date incorrect format to update", ),
    pytest.param(incorrect_birthdate_fake_leap_year, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Fake leap date incorrect format to update", ),
    pytest.param(incorrect_birthdate_future_date, ERROR_BIRTHDATE_WRONG_FORMAT_FUTURE,
                 id="Future date incorrect format to update", )
])
def test_update_not_exist_user_with_incorrect_birthdate_format(remove_default_user, args, expected_result):
    response = requests.put(hello_requests_url + default_username, json={"dateOfBirth": args})
    if not args == incorrect_birthdate_future_date:
        if not response.status_code == http.HTTPStatus.BAD_REQUEST:
            errors.append(f"Wrong status code, response code is {response.status_code}")
    else:
        if not response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY:
            errors.append(f"Wrong status code, response code is {response.status_code}")
    if expected_result not in response.text:
        errors.append(f"Not expected result, result is {response.text}")
    if not user_not_in_base(default_username):
        errors.append(f"User birthdate changed, result is {response.text}")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))


"""
Тест кейс 9 Обновление данных существующего пользователя при некорректном формате даты рождения
Негативный сценарий при котором не должно происходить обновление данных существующего пользователя 
при некорректном формате даты рождения
"""
@pytest.mark.parametrize("args, expected_result", [
    pytest.param(incorrect_birthdate_format, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Incorrect birthdate format to update", ),
    pytest.param(incorrect_birthdate_not_exists, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Not existing date incorrect format to update", ),
    pytest.param(incorrect_birthdate_letters, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Random numerics date incorrect format to update", ),
    pytest.param(incorrect_birthdate_fake_leap_year, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Fake leap date incorrect format to update", ),
    pytest.param(incorrect_birthdate_future_date, ERROR_BIRTHDATE_WRONG_FORMAT_FUTURE,
                 id="Future date incorrect format to update", )
])
def test_update_exists_user_with_incorrect_birthdate_format(remove_default_user, create_default_user,
                                                            args, expected_result):
    response = requests.put(hello_requests_url + default_username, json={"dateOfBirth": args})
    if not args == incorrect_birthdate_future_date:
        if not response.status_code == http.HTTPStatus.BAD_REQUEST:
            errors.append(f"Wrong status code, response code is {response.status_code}")
    else:
        if not response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY:
            errors.append(f"Wrong status code, response code is {response.status_code}")
    if expected_result not in response.text:
        errors.append(f"Not expected result, result is {response.text}")
    if not user_exists_not_changed_and_alone(default_username, args):
        errors.append(f"User birthdate changed, result is {response.text}")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))
