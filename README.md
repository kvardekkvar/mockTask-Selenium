#  Автотесты для сайта кошелек.ру

Написаны автотесты для негативных проверок страницы регистрации

## Описание проекта:

* pages - папка с объектами Page Object
* tests - папка с тестами
* tests/conftest.py - файл с фикстурами
* Dockerfile - image докера для запуска тестов

## Системные требования:
Docker (v4.35.1) и docker-compose

## Инструкции по запуску:

1. Склонировать репозиторий в отдельную папку: `git clone https://github.com/kvardekkvar/mockTask-Selenium`
2. Открыть эту папку в терминале/командной строке
3. Выполнить команду для прогона тестов `docker-compose up test_run`
4. После завершения прогона выполнить команду для просмотра allure-отчета `docker-compose up allure -d`

После выполнения пункта 4 аллюр-отчет доступен по адресу https://localhost:9092