import requests
from tests.consts_and_variables import *

"""
Вспомогательные функции
"""


def create_user(url, username, birthdate):
    return requests.post(url + username,
                         json={"dateOfBirth": birthdate})


def correct_user_created(username, birthdate):
    response = requests.get(users_list_url)
    response_body = response.json()
    for item in response_body['users']:
        if username in item['username']:
            if birthdate in item['dateOfBirth']:
                return True
            else:
                return False
    return False


def user_exists_not_changed_and_alone(username, newdate):
    user_count = 0
    response = requests.get(users_list_url)
    response_body = response.json()
    for item in response_body['users']:
        if username in item['username']:
            user_count += 1
    if user_count == 1:
        for item in response_body['users']:
            if username in item['username']:
                if newdate not in item['dateOfBirth']:
                    return True
                else:
                    return False
        return False
    else:
        return False


def user_exists_changed_and_alone(username, newdate):
    user_count = 0
    response = requests.get(users_list_url)
    response_body = response.json()
    for item in response_body['users']:
        if username in item['username']:
            user_count += 1
    if user_count == 1:
        for item in response_body['users']:
            if username in item['username']:
                if newdate in item['dateOfBirth']:
                    return True
                else:
                    return False
        return False
    else:
        return False


def user_not_in_base(username):
    response = requests.get(users_list_url)
    response_body = response.json()
    for item in response_body['users']:
        if username in item['username']:
            return False
    return True
