import pytest
import http
from funcs.birthday_list_api_helper import *
from consts_and_variables import *

"""
Тесты посвященные удалению пользователя из БД
Каждый тест соответсвует тест-кейсу из документации
Включает тест-кейсы с 13 по 14
"""


"""
Тест кейс 13 Удаление существующего пользователя из БД
Позитивный сценарий в котором пользователь с заданным именем должен быть удален из БД
"""
def test_delete_existing_user(create_default_user, remove_default_user_response):
    if not remove_default_user_response.status_code == http.HTTPStatus.OK:
        errors.append(f"Wrong status code, response code is {remove_default_user_response.status_code}")
    if DELETE_SUCCESSFULLY not in remove_default_user_response.text:
        errors.append(f"Not expected result, result is {remove_default_user_response.text}")
    if not user_not_in_base(default_username):
        errors.append("User not deleted")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))


"""
Тест кейс 14 Удаление пользователя не существующего в БД
Негативный сценарий при котором не должно быть возможности удалить несуществующего пользователя
"""
def test_delete_not_existing_user(remove_default_user_response):
    if not remove_default_user_response.status_code == http.HTTPStatus.NOT_FOUND:
        errors.append(f"Wrong status code, response code is {remove_default_user_response.status_code}")
    if ERROR_USER_DOES_NOT_EXISTS not in remove_default_user_response.text:
        errors.append(f"Not expected result, result is {remove_default_user_response.text}")
    if not user_not_in_base(default_username):
        errors.append("User not deleted")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))
