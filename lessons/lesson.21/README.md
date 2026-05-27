python3 -m venv .venv
python -m venv myvenv

source ./.venv/bin/activate
source ./myvenv/Script/activate.ps1

# Установка зависимостей
pip install fastapi
pip install "uvicorn[standard]"

# Запуск проекта
uvicorn main:app --reload

# Проект
http://localhost:8000/


# Документация
http://localhost:8000/docs
http://localhost:8000/redoc

# Query параметры
https://ya.ru/search/?text=python&lang=ru
http://localhost:8000/about/2/21/?name=Bob&age=32


pip install jinja2
pip install fastapi[all]