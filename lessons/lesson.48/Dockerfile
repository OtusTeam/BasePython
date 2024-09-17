FROM tiangolo/uwsgi-nginx-flask:python3.11

RUN pip install --upgrade pip

# COPY poetry.lock pyproject.toml ./
COPY requirements.txt ./requirements.txt

# RUN poetry install
RUN pip install -r requirements.txt

COPY ./prestart.sh ./prestart.sh

COPY ./ ./
