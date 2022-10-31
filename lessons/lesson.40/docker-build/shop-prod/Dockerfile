FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY ./ /app
