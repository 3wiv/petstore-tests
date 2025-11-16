README.md
Описание проекта

Этот проект содержит набор автоматизированных тестов для публичного демо-API Swagger Petstore
(https://petstore.swagger.io/v2).

Тесты написаны на Python 3, с использованием Pytest и requests.
Покрыты операции API: создание, получение, обновление и удаление сущностей. Сами тесты включают в себя как простые, так и параметризированные.

## Что покрывают тесты
Pet (питомцы)

POST /pet — создание

GET /pet/{petId} — получение

PUT /pet — обновление

DELETE /pet/{petId} — удаление

GET /pet/findByStatus — выборка по статусу

## Стек проекта
- Python 3
- Pytest
- requests

## Структура проекта
petstore-tests
|-- src
|
|  |-- api_client.py
|  \-- data_generators.py
|
|-- tests
|  |-- test_pets.py
|
|-- conftest.py  
|-- .gitignore 
|-- requirements.txt
|-- pytest.ini
\-- README.md

## Установка и запуск

1. Клонировать репозиторий:

    ```bash
    git clone https://github.com/3wiv/petstore-tests.git
    cd petstore-tests
    ```

2. Создать виртуальное окружение:

    ```bash
    python -m venv venv
    ```

3. Активировать окружение:

    **Windows:**
    ```bash
    venv\Scripts\activate
    ```

    **Linux / macOS:**
    ```bash
    source venv/bin/activate
    ```

4. Установить зависимости:

    ```bash
    pip install -r requirements.txt
    ```

5. Запустить тесты:

    Всевозможные тесты:
    ```bash
    pytest -v
    ```

    По маркерам:
    ```bash
    pytest -m pet
    ```
## Особенности работы с Petstore API

Демо-API Petstore - сервис, который используется для обучения и примеров. В связи с этим он работает не так стабильно, как полноценное рабочее окружение. Иногда ответы сервера могут отличаться от ожидаемых: например, после создания сущности запрос на её получение может вернуть 404, или может происходить задержка в ответе.
В остальном тесты запускаются локально и работают без дополнительной конфигурации.
