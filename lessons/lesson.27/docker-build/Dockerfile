FROM tiangolo/uwsgi-nginx-flask:python3.9

ENV PYTHONBUFFERED=1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
