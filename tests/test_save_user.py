import pytest
import http
from funcs.birthday_list_api_helper import *
from consts_and_variables import *

"""
Тесты посвященные сохранению имени пользователя и его даты рождения в БД
Каждый тест соответсвует тест-кейсу из документации
Включает тест-кейсы со 2 по 5
"""


"""
Тест кейс 2 Сохранение нового пользователя
Позитивный сценарий в котором создается пользователь с корректными форматами даты и имени
"""
@pytest.mark.parametrize("args, expected_result", [
    pytest.param(default_username, OK_USER_ADDED,
                 id="User created with correct username format", )
])
def test_correct_create_user(remove_default_user, args, expected_result, create_default_user_response):
    if not create_default_user_response.status_code == http.HTTPStatus.CREATED:
        errors.append(f"Wrong status code, response code is {create_default_user_response.status_code}")
    if expected_result not in create_default_user_response.text:
        errors.append(f"Not expected result, result is {create_default_user_response.text}")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))


"""
Тест кейс 3 Добавление пользователя с именем, уже существующем в БД
Негативный сценарий в котором проверяется добавление пользователя с именем, уже существующем в БД
"""
def test_try_to_save_already_existing_user(remove_default_user, create_default_user, create_default_user_response,
                                           create_default_2012_user_response):
    if not create_default_user_response.status_code == http.HTTPStatus.CONFLICT:
        errors.append(f"Wrong status code, response code is {create_default_user_response.status_code}")
    if ERROR_USER_ALREADY_EXISTS not in create_default_user_response.text:
        errors.append(f"Not expected result, result is {create_default_user_response.text}")

    if not create_default_2012_user_response.status_code == http.HTTPStatus.CONFLICT:
        errors.append(f"Wrong status code, response code is {create_default_2012_user_response.status_code}")
    if ERROR_USER_ALREADY_EXISTS not in create_default_2012_user_response.text:
        errors.append(f"Not expected result, result is {create_default_2012_user_response.text}")
    if not user_exists_not_changed_and_alone(default_username, default_birthdate_2012):
        errors.append(f"User birthdate changed, result is {create_default_2012_user_response.text}")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))


"""
Тест кейс 4 Добавление пользователя с некорректным форматом имени
Негативный сценарий в котором проверяется верность формата имени при создании пользователя
"""
@pytest.mark.parametrize("args, expected_result", [
    pytest.param(incorrect_username_num, ERROR_USERNAME_WRONG_FORMAT,
                 id="Numeric username incorrect format", ),
    pytest.param(incorrect_username_symbols, ERROR_USERNAME_WRONG_FORMAT,
                 id="Symbolic username incorrect format", ),
    pytest.param(incorrect_username_def_with_numbers, ERROR_USERNAME_WRONG_FORMAT,
                 id="Username with numbers incorrect format", ),
    pytest.param(incorrect_username_def_with_symbols, ERROR_USERNAME_WRONG_FORMAT,
                 id="Username with symbols incorrect format", )
])
def test_incorrect_create_user_username_variants(remove_default_user, args, expected_result):
    response = create_user(hello_requests_url, args, default_birthdate)
    if not response.status_code == http.HTTPStatus.BAD_REQUEST:
        errors.append(f"Wrong status code, response code is {response.status_code}")
    if expected_result not in response.text:
        errors.append(f"Not expected result, result is {response.text}")
    if not user_not_in_base(args):
        errors.append("ERROR, incorrect user added to base")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))


"""
Тест кейс 5 Добавление пользователя с некорректным форматом даты рождения
Негативный сценарий в котором при некорректном формате даты рождения не должна создаваться новая запись в БД
"""
@pytest.mark.parametrize("args, expected_result", [
    pytest.param(incorrect_birthdate_format, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Incorrect birthdate format to save", ),
    pytest.param(incorrect_birthdate_not_exists, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Not existing date incorrect format to save", ),
    pytest.param(incorrect_birthdate_letters, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Random numerics date incorrect format to save", ),
    pytest.param(incorrect_birthdate_fake_leap_year, ERROR_BIRTHDATE_WRONG_FORMAT,
                 id="Fake leap date incorrect format to save", ),
    pytest.param(incorrect_birthdate_future_date, ERROR_BIRTHDATE_WRONG_FORMAT_FUTURE,
                 id="Future date incorrect format to save", ),
])
def test_save_user_with_incorrect_birthdate_format(remove_default_user, args, expected_result):
    response = create_user(hello_requests_url, default_username, args)
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
