FROM tiangolo/uwsgi-nginx-flask:python3.9

WORKDIR /app

RUN pip install -U pip
RUN pip install setuptools wheel

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./
