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

# Переменные окружения
ENV DEBUG=False

# Команда по умолчанию
CMD ["python", "app.py"]

# Точка входа (не перезаписывается)
ENTRYPOINT ["python", "app.py"]
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

---

## 🔄 docker-compose

### Основные команды:
```bash
# Запустить сервисы
docker-compose up
docker-compose up -d        # В фоне
docker-compose up --build  # С пересборкой

# Остановить сервисы
docker-compose down
docker-compose down -v      # С удалением volumes

# Показать статус
docker-compose ps

# Логи
docker-compose logs
docker-compose logs -f service-name

# Выполнить команду в сервисе
docker-compose exec web bash
```

### Пример docker-compose.yml:
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=True
      - DATABASE_URL=postgresql://user:password@db:5432/myapp
    depends_on:
      - db
    volumes:
      - .:/app
    
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=myapp
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

---

## 📦 Volume и сети

### Работа с Volume:
```bash
# Создать volume
docker volume create my-data

# Список volumes
docker volume ls

# Удалить volume
docker volume rm my-data

# Примонтировать volume
docker run -v my-data:/data ubuntu:20.04

# Bind mount (папка хоста)
docker run -v /host/path:/container/path ubuntu:20.04
```

### Работа с сетями:
```bash
# Создать сеть
docker network create my-network

# Список сетей
docker network ls

# Подключить контейнер к сети
docker run --network my-network ubuntu:20.04

# Информация о сети
docker network inspect my-network
```

---

## 🛠️ Практические примеры

### FastAPI + PostgreSQL:
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/myapp
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@example.com
      - PGADMIN_DEFAULT_PASSWORD=admin
    ports:
      - "8080:80"
    depends_on:
      - db

volumes:
  postgres_data:
```

### Nginx + приложение:
```yaml
version: '3.8'

services:
  app:
    build: .
    expose:
      - "8000"
    
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - app
```

```nginx
# nginx.conf
events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        
        location / {
            proxy_pass http://app:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

### Development с hot reload:
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    environment:
      - DEBUG=True
```

---

## 🔧 Оптимизация

### Многоступенчатая сборка:
```dockerfile
# Стадия сборки
FROM python:3.11 AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Продакшн стадия
FROM python:3.11-slim

WORKDIR /app

# Копируем установленные пакеты
COPY --from=builder /root/.local /root/.local

# Добавляем в PATH
ENV PATH=/root/.local/bin:$PATH

COPY . .

CMD ["python", "app.py"]
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

## 🏷️ Переменные окружения

### В docker-compose.yml:
```yaml
services:
  app:
    build: .
    environment:
      - DEBUG=True
      - DATABASE_URL=postgresql://user:pass@db/myapp
    env_file:
      - .env
```

### Файл .env:
```bash
DEBUG=True
SECRET_KEY=my-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/myapp
```

---

## 🧹 Очистка системы

### Очистка ресурсов:
```bash
# Удалить неиспользуемые образы
docker image prune

# Удалить остановленные контейнеры
docker container prune

# Удалить неиспользуемые volumes
docker volume prune

# Удалить неиспользуемые сети
docker network prune

# Полная очистка системы
docker system prune -a

# Показать использование места
docker system df
```

---

## 📊 Мониторинг и отладка

### Статистика использования:
```bash
# Статистика контейнеров
docker stats

# Информация о контейнере
docker inspect container-id

# Процессы в контейнере
docker top container-id
```

### Отладка:
```bash
# Войти в контейнер
docker exec -it container-id bash

# Скопировать файлы из контейнера
docker cp container-id:/path/to/file /local/path

# Скопировать файлы в контейнер
docker cp /local/path container-id:/path/to/file
```

---

## ⚠️ Важные моменты

- Используйте минимальные базовые образы (alpine, slim)
- Не запускайте контейнеры от root пользователя
- Используйте .dockerignore для исключения лишних файлов
- Группируйте RUN команды для уменьшения слоев
- Кешируйте зависимости отдельно от кода приложения
- Используйте docker-compose для многоконтейнерных приложений
- Регулярно обновляйте базовые образы для безопасности 