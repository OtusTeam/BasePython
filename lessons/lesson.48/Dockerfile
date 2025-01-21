from python:3.12

# SHELL ["/bin/bash", "-c"]

RUN apt-get update

COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

# RUN python -m venv venv
# RUN source venv/bin/activate
# RUN pip3 install --upgrade pip
# RUN pip3 install poetry
# RUN poetry install

RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry install
# RUN source `poetry env info --path`/bin/activate

COPY ./fastapi-app ./