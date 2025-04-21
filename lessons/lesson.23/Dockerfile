FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
#COPY pyproject.toml poetry.lock ./  #копируем файлы poetry

RUN pip install --no-cache-dir -r requirements.txt
#RUN poetry install --no-dev

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]