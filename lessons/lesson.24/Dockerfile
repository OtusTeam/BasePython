FROM python:3.9.5-buster

WORKDIR /app

RUN pip install -U pip setuptools

COPY requirements.txt .
RUN pip install -r requirements.txt

#COPY ./web-app/pyproject.toml .
#COPY ./web-app/poetry.lock .
#
#RUN poetry install

COPY ./web-app .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

ENTRYPOINT ["./entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]
