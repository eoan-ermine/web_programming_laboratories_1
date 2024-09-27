PROJECT_NAME ?= web_programming_laboratories_1

all:
	@echo "make format\t— Format code with black & isort"


format:
	poetry run python3 -m black $(PROJECT_NAME)
	poetry run python3 -m isort $(PROJECT_NAME)