# Занятие "Docker"

## 🐳 Основные команды Docker

### Получить информацию о Docker:
```bash
docker --version

docker version

docker info
```

### Работа с контейнерами:
```bash
# Запустить контейнер
docker run alpine:3.20
docker run -it alpine:3.20 sh  # Интерактивно
docker run -d redis                     # В фоне (daemon)
docker run -p 8080:80 redis            # Проброс портов

# Список контейнеров
docker ps           # Активные
docker ps -a        # Все (включая остановленные)

# Остановить/запустить контейнер
docker stop container-id-or-name
docker start container-id-or-name
docker restart container-id-or-name

# Удалить контейнер
docker rm container-id

# Логи контейнера
docker logs container-id-or-name
docker logs -f container-id-or-name  # Следить за логами

# Выполнить команду sh в контейнере
docker exec -it container-id-or-name sh
```

### Работа с образами:
```bash
# Найти образ
docker search redis

# Скачать образ
docker pull redis:latest

# Список образов
docker images

# Удалить образ
docker rmi image-name-or-id

# Собрать образ
docker build -t myapp-flask:v1 .

# Запустить собранный образ
docker run -d -p 8000:8000 --name my-flask-1 myapp-flask:v1

# Посмотреть историю образа
docker history my-app
```

---

## 📝 Dockerfile

### Пример Dockerfile для Python/Flask:
```dockerfile
# Базовый образ
FROM python:3.12-slim

# Рабочая директория
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Декларируем порт
EXPOSE 8000

# Запускаем приложение
CMD ["python", "main.py"]
```

### Dockerfile с Poetry:
```dockerfile
# Базовый образ
FROM python:3.12-slim

# Рабочая директория
WORKDIR /app

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем файлы конфигурации
COPY pyproject.toml ./

# Устанавливаем зависимости
RUN poetry install --no-root

# Копируем код
COPY . .

# Декларируем порт
EXPOSE 8000

# Запускаем приложение
CMD ["poetry", "run", "python", "main.py"]
```