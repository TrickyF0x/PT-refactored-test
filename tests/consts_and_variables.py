import pytest
from datetime import datetime

"""
Данный файл содержит переменные и значения по умолчанию, 
которые используются в тестах.
"""

basic_url = "http://129.146.247.102:5000/"
users_list_url = basic_url + "users"
hello_requests_url = basic_url + "hello/"

default_username = "smarthostagelover"
not_default_username = "notsmarthostagelover"
incorrect_username_num = "123456"
incorrect_username_symbols = r"*\&^(%"
incorrect_username_def_with_numbers = "a1b2c3d4e5"
incorrect_username_def_with_symbols = "=_anton_="

default_birthdate = '1977-07-07'
default_birthdate_2012 = '2012-12-30'
incorrect_birthdate_format = '1 january 2013'
incorrect_birthdate_not_exists = '2020-06-52'
incorrect_birthdate_letters = '123456'
incorrect_birthdate_fake_leap_year = '2019-02-29'
incorrect_birthdate_future_date = '2045-11-30'
incorrect_birthdate_now = datetime.date(datetime.now()).strftime("%Y-%m-%d")

OK_USER_ADDED = "New user '" + default_username + "' was added successfully."
HAPPY_BIRTHDAY = "Hello, " + default_username + "! Happy birthday!"
HAPPY_BIRTHDAY_NOT_TODAY_LEAP = "Hello," + default_username + "! Your birthday is in 5 day(s)."
HAPPY_BIRTHDAY_NOT_TODAY_DEFAULT = "Hello," + default_username + "! Your birthday is in 5 day(s)."
DELETE_SUCCESSFULLY = "User '" + default_username + "' was deleted successfully."

errors = []
ERROR_USERNAME_WRONG_FORMAT = "Username must be a string containing only letters."
ERROR_USER_ALREADY_EXISTS = "User already exists. Use 'PUT' method for updating the date of birth."
ERROR_USER_DOES_NOT_EXISTS = "User with username '" + default_username + "' does not exist."
ERROR_BIRTHDATE_WRONG_FORMAT = "JSON field 'dateOfBirth' is missing or value not in 'YYYY-MM-DD' format."
ERROR_BIRTHDATE_WRONG_FORMAT_FUTURE = "Date of birth must be a date before the today date."
