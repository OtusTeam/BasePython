FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
#COPY pyproject.toml .


RUN pip install --no-cache-dir -r requirements.txt
#RUN poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]