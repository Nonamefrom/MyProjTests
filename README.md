# e2e

Проект для e2e тестов проектов группы «Маркетинг»

## Как с этим работать

- `make setup`
- `make build`
- `make install`
- `make up`

Поздравляем, после команд у вас запущен Allure (для просмотра отчетов по тестам) и контейнер для работы с python

## Как работать с тестами

Для запуска тестов:
`pipenv run pytest --alluredir=allure-results --browser chrome_headless`

## Как смотреть отчеты Allure

- На `http://localhost:5050` будет доступ `allure`
- На `http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html` последний отчет
- На `http://localhost:5050/allure-docker-service/projects/default/` история отчетов (если есть)

## Основано на

Фреймворки:

- [Allure](https://www.allure.com/)
- [Selenium](https://www.selenium.dev/)
- [Pytest](https://docs.pytest.org/en/7.1.x/)

Docker:

- [Selenium-Python-Example](https://github.com/nirtal85/Selenium-Python-Example)
- [allure-docker-service](https://github.com/fescobar/allure-docker-service)
