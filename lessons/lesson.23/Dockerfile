# Указываем базовый образ Python версии 3.9
FROM python:3.12

# Устанавливаем переменные окружения для оптимизации поведения Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

#Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем Poetry. Используем последнюю стабильную версию
RUN pip install --upgrade pip setuptools whell && \
    pip install "poetry==1.8.3"

# Отключаем создание виртуальных окружений внутри контейнера, поскольку Poetry будет использовать окружение контейнера
RUN poetry config virtualenvs.create false

# Копируем только файлы pyproject.toml и poetry.lock для установки зависимостей
# Этот слой будет пересобран только в случае изменения зависимостей
COPY poetry.lock pyproject.toml ./

# Устанавливаем зависимости, используя Poetry
# Этот шаг будет пересобран, только если изменились pyproject.toml или poetry.lock
RUN poetry install --no-root

# Копируем остальной исходный код приложения
# Этот слой будет пересобран каждый раз, когда изменится код приложения
COPY . .

#Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Запускаем команду для старта сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]