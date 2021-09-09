FROM tiangolo/uwsgi-nginx-flask
FROM python:3.9-buster

WORKDIR /app

RUN pip install -U pip
RUN pip install setuptools wheel

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./
COPY entrypoint.sh /var/entrypoint.sh
RUN chmod +x /var/entrypoint.sh

ENTRYPOINT ["/var/entrypoint.sh"]
