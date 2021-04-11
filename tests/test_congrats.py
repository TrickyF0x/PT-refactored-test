import http
from consts_and_variables import *
import calendar

"""
Тесты посвященные получению поздравления с днем рождения для пользователя
Каждый тест соответсвует тест-кейсу из документации
Включает тест-кейсы с 10 по 12
"""


"""
Тест кейс 10 Получение поздравления с днем рождения
Позитивный сценарий в котором текущая дата совпадает с датой дня рождения пользователя, 
т.о. должно появиться поздравление пользователя с днем рождения
"""
def test_happy_birthday_today(remove_default_user, year_ago_date, create_new_user_year_ago, get_default_user_response):
    if not get_default_user_response.status_code == http.HTTPStatus.OK:
        errors.append(f"Wrong status code, response code is {get_default_user_response.status_code}")
    if HAPPY_BIRTHDAY not in get_default_user_response.text:
        errors.append(f"Not expected result, result is {get_default_user_response.text}")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))


"""
Тест кейс 11 Получение информации о количестве дней до дня рождения
Позитивный сценарий в котором текущая дата не является датой дня рождения пользователя, 
т.о. должна появиться информации о количестве дней до дня рождения
"""
def test_happy_birthday_not_today(remove_default_user, almost_year_ago, current_year,
                                  create_new_user_almost_year_ago, get_default_user_response):
    if not get_default_user_response.status_code == http.HTTPStatus.OK:
        errors.append(f"Wrong status code, response code is {get_default_user_response.status_code}")
    if calendar.isleap(current_year):
        if HAPPY_BIRTHDAY_NOT_TODAY_LEAP not in get_default_user_response.text:
            errors.append(f"Not expected result, result is {get_default_user_response.text}")
        else:
            if HAPPY_BIRTHDAY_NOT_TODAY_DEFAULT not in get_default_user_response.text:
                errors.append(f"Not expected result, result is {get_default_user_response.text}")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))


"""
Тест кейс 12 Получение поздравление для несуществующего пользователя
Негативный сценарий при котором не должно быть информации о дне рождения пользователя, которого нет в БД
"""
def test_happy_birthday_to_not_exists_user(remove_default_user, get_default_user_response):
    if not get_default_user_response.status_code == http.HTTPStatus.NOT_FOUND:
        errors.append(f"Wrong status code, response code is {get_default_user_response.status_code}")
    if ERROR_USER_DOES_NOT_EXISTS not in get_default_user_response.text:
        errors.append(f"Not expected result, result is {get_default_user_response.text}")
    assert not errors, "Errors occured:\n{}".format("\n".join(errors))
