FROM python:alpine

RUN apk add --no-cache make bash

RUN adduser -D -h /home/userTest userTest

RUN mkdir -p /home/userTest/.cache && \
    chmod -R a+w /home/userTest/.cache 

ENV PATH="/home/userTest/.local/bin:$PATH"

USER userTest

WORKDIR /app/test

COPY pyproject.toml /app/test

RUN wget -qO- https://install.python-poetry.org | python3 -

RUN poetry install --no-root

ENV PYTHONPATH=/app/test

ENV POETRY_CACHE_DIR=/home/userTest/.cache/pypoetry

ENV POETRY_VIRTUALENVS_PATH=/home/userTest/.cache/pypoetry/virtualenvs

ENTRYPOINT ["make", "test"]