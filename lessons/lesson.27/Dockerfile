FROM python:3.9-buster

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x prestart.sh

ENV CONFIG="ProductionConfig"

ENTRYPOINT ["bash", "prestart.sh"]
CMD python app.py
