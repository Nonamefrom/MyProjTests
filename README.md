# e2e

Проект для e2e тестов проектов группы «Маркетинг»

## Как с этим работать

- `make setup`
- `make build`
- `make up`

Поздравляем, после команд у вас запущен Allure (для просмотра отчетов по тестам) и контейнер для работы с python

## Как работать с тестами

Для запуска тестов:

- `make run-python`
- `make test`

Таким образом вы войдете в контейнер с python. Вторая команда запускает тесты. Что делает команда можно посмотреть в файле `Makefile`

## Как смотреть отчеты Allure

- На `http://localhost:5050` будет доступ `allure`
- На `http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html` последний отчет
- На `http://localhost:5050/allure-docker-service/projects/default/` история отчетов (если есть)

## Selenium hub

- На `http://localhost:4444`
- `http://localhost:7900/?autoconnect=1&resize=scale&password=secret`

## Основано на

Фреймворки:

- [Allure](https://www.allure.com/)
- [Selenium](https://www.selenium.dev/)
- [Pytest](https://docs.pytest.org/en/7.1.x/)

## Разработка на Windows/MacOS

- В  `.env` файле установите правильный образ (для MacOS `seleniarm/*`, для Windows/linux `selenium/*`)
