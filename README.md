# API тесты с использованием pytest и requests, посвященные тестовому заданию Positive Technologies

Тестовое задание заключается в автоматизации тестов к написанным тест-кейсам, а именно в тестировании сервиса, 
взаимодействие с которым осуществляется через HTTP-запросы.


### Структура проекта.

**funcs/** - файлы вспомогательных функций<br/>
**tests/** - папка содержащая тесты, файл констант и conftest для фикстур<br/>
**Dockerfile** - файл для контейнеризации в docker<br/>
**Тест-кейсы.docx** - задокументированные тест-кейсы, которым соотвествуют тесты<br/>
**requirements.txt** - файл с требованиями к среде<br/>

-------------------------------------

### Описание тестов

1. test_get_user_list.py - получение списка пользователей и их дат рождения из БД (1й тест-кейс)
2. test_save_user.py - сохранение имени пользователя и его даты рождения в БД (тест-кейсы со 2 по 5)
3. test_update_user.py - обновление данных даты рождения пользователя в БД (тест-кейсы со 6 по 9)
4. test_congrats.py - получение поздравления с днем рождения для пользователя (тест-кейсы с 10 по 12)
5. test_delete_user.py - удаление пользователя из БД (тест-кейсы с 13 по 14)

-------------------------------------

### Примечание

1. Корректный формат имени пользователя - только буквы
2. Корректный формат даты YYYY-MM-DD и должна быть датой до текущего дня
3. Константы, переменные и адрес можно изменить в файле tests/consts_and_variables.py
4. Ошибки логируются в файл tests/failures
5. По умолчанию публичный адрес сервиса: 129.146.247.102:5000

-------------------------------------

### Запуск в Docker

1. docker build -t test_birthday_list .
2. docker run test_birthday_list

-------------------------------------


_Нет предела совершенству и последует дальнейший рефакторинг._
