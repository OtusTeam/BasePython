# Создание виртуального окружения
python3 -m venv .myvenv  # MacOs, Linux
python -m venv .myvenv   # Windows

# Активация виртуального окружения
source ./.myvenv/bin/activate  # MacOs, Linux
./.myvenv/Scripts/activate    # Windows CMD
./.myvenv/Scripts/Activate.ps1    # Windows PowerShell

# Деактивация виртуального окружения
deactivate

# Установить зависимость с помощью pip 
pip install requests

# Установить конкретную версию зависимости с помощью pip 
pip install requests==2.31

# Обновить зависимость с помощью pip 
pip install --upgrade requests

# Посмотреть список зависимостей 
pip list

# Сохранить список зависимостей в файл
pip freeze > requirements.txt

# Установить список зависимостей из файла requirements.txt
pip install -r ./requirements.txt

# Сайт poetry
https://python-poetry.org/docs/#installing-with-the-official-installer

# Установить poetry в системы MacOs, Linux, Windows
curl -sSL https://install.python-poetry.org | python3 -

# Установить poetry в системы Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# Проверить версию poetry
poetry --version

# Создать новый проект poetry ./new_project
poetry new ./new_project

# Инициализировать проект poetry 
poetry init

# Установить зависимость в проект poetry 
poetry add fastapi

# Удалить зависимость в проекте poetry 
poetry remove fastapi

# Добавить зависимость в проект poetry  в группу 
poetry add pytest --group dev
poetry add ruff --group lint

# Установить зависимости из pyproject.toml в проект poetry 
poetry install

# Установить зависимости из pyproject.toml в проект poetry без группы dev
poetry install --without dev