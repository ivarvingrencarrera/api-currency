FROM python:3.11-slim as builder
LABEL maintainer="Ivar Vingren Carrera <ivar.carrera@gmail.com>"

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --no-install-recommends build-essential libpq-dev curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python -m venv /venv

ENV POETRY_VERSION=1.4.2
ENV POETRY_HOME=/opt/poetry
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV POETRY_VERSION=1.4.2
RUN curl https://install.python-poetry.org | python -

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN . /venv/bin/activate; \
    $POETRY_HOME/bin/poetry install --only main --no-interaction

# ---------------------------------------------------------

FROM python:3.11-slim as final
ENV PATH=/venv/bin:${PATH}

WORKDIR /app
USER nobody
COPY --chown=nobody:nogroup src/ ./src

EXPOSE 5000

ENTRYPOINT [ "python", "src/main_api.py"]