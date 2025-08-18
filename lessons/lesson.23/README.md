# Шпаргалка: Docker

## 🐳 Основные команды Docker

### Работа с образами:
```bash
# Скачать образ
docker pull ubuntu:20.04

# Список образов
docker images

# Удалить образ
docker rmi ubuntu:20.04

# Построить образ
docker build -t my-app .

# Посмотреть историю образа
docker history my-app
```

### Работа с контейнерами:
```bash
# Запустить контейнер
docker run ubuntu:20.04
docker run -it ubuntu:20.04 /bin/bash  # Интерактивно
docker run -d nginx                     # В фоне (daemon)
docker run -p 8080:80 nginx            # Проброс портов

# Список контейнеров
docker ps           # Активные
docker ps -a        # Все (включая остановленные)

# Остановить/запустить контейнер
docker stop container-id
docker start container-id
docker restart container-id

# Удалить контейнер
docker rm container-id

# Логи контейнера
docker logs container-id
docker logs -f container-id  # Следить за логами

# Выполнить команду в контейнере
docker exec -it container-id /bin/bash
```

---

## 📝 Dockerfile

### Основные инструкции:
```dockerfile
# Базовый образ
FROM python:3.11-slim

# Рабочая директория
WORKDIR /app

# Копирование файлов
COPY requirements.txt .
COPY . .

# Выполнить команду при сборке
RUN pip install -r requirements.txt

# Открыть порт
EXPOSE 8000

# Команда по умолчанию
CMD ["python", "app.py"]

```

### Пример Dockerfile для Python/FastAPI:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Открываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Dockerfile с Poetry:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Устанавливаем Poetry
RUN pip install poetry

# Копируем файлы конфигурации
COPY pyproject.toml poetry.lock ./

# Настраиваем Poetry
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости
RUN poetry install --only=main

# Копируем код
COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```



### .dockerignore:
```
# .dockerignore
__pycache__/
*.pyc
.git/
.venv/
node_modules/
README.md
.env
.pytest_cache/
```

### Кеширование слоев:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Сначала копируем зависимости (кешируется)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Потом копируем код (кеш инвалидируется чаще)
COPY . .

CMD ["python", "app.py"]
```

---

## 🧹 Очистка ресурсов:
```bash
# Удалить неиспользуемые образы
docker image prune

# Удалить остановленные контейнеры
docker container prune
```

---

## ⚠️ Важные моменты

- Используйте минимальные базовые образы (alpine, slim)
- Используйте .dockerignore для исключения лишних файлов
- Кешируйте зависимости отдельно от кода приложения
- Регулярно обновляйте базовые образы для безопасности 
