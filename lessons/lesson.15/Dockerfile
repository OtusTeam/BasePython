FROM python:3.10-buster

WORKDIR /var/app

# ARG - для этапа сборки
# ENV - на этапе выполнения

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


RUN chmod +x ./prestart.sh
ENTRYPOINT ["./prestart.sh"]
#CMD uvicorn main:app
CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
