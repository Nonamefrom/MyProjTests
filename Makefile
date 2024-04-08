# Setup
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DOCKER_COMPOSE := docker-compose
DOCKER_COMMAND_TEMPLATE := docker-compose exec e2e-python bash
DOCKER_COMPOSE_FILE := $(ROOT_DIR)/docker-compose.yml
ENV_FILE := $(ROOT_DIR)/.env
# End setup

.PHONY: help setup install install-v build up start down clean logs ps run-python all

.DEFAULT_GOAL := help

help: ## Show this help message.
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

setup: ## Копирование файлов
	@[ -f $(ENV_FILE) ] && echo .env exists || cp .env.template .env

build: ## Запускает сборку образа python
	@docker build -f ./docker/local/python/Dockerfile --progress=plain -t e2e-python .

run-python: ## Открыть bash в контейнере python
	@${DOCKER_COMMAND_TEMPLATE}

up: ## Запускает docker-compose в текущем shell
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up

start: ## Запускает docker-compose в daemon режиме
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up -d

down: ## Останавливает docker-compose
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down

clean: ## Останавливает контейнеры и удаляет все volumes описанные в docker-compose файле
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down -v

logs: ## Показывает логи всех контейнеров в follow режиме в кол-ве 50 штук
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) logs -f --tail 50

ps: ## Выводит список контейнеров и их статусы из docker-compose файла
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) ps

test: ## Запускает тесты с генерацией отчетов
	@pytest ./tests/ --alluredir="./allure-results"

lint: ## Запуск pylint для линтинга
	@pylint "./**/*.py"

all: ## Настройка окружения, сборка, установка зависимостей и запуск контейнеров в одной команде
	make setup
	make build
	make install
	make start
