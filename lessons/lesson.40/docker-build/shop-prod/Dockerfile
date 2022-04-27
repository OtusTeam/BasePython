FROM tiangolo/meinheld-gunicorn-flask:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install greenlet==0.4.16

COPY ./ /app
