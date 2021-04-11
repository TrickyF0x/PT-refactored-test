import requests
import pytest
import http
from consts_and_variables import *

"""
Тест посвященный получению списка пользователей и их дат рождения из БД

Тест соответсвует 1му тест-кейсу из документации
"""
def test_get_users_list(get_users_list_response):
    response_body = get_users_list_response.json()
    if get_users_list_response.status_code == http.HTTPStatus.OK:
        assert "userName", "dateOfBirth" in response_body.keys()
