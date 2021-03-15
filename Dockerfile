FROM python:3.7

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
RUN pip install poetry

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /usr/src/app

RUN poetry run task init_db

CMD [ "poetry", "run", "task", "start" ]