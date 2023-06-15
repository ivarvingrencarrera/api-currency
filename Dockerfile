#
# Base image
#

FROM python:3.11-buster AS base
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y make \
    && rm -rf /var/lib/apt/lists/*

#
# Development image
#

FROM base AS development 
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python - \
    && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.in-project true \
    && poetry install --without doc --no-interaction --no-ansi -vvv \
    && poetry export --only main -f requirements.txt > requirements.txt
COPY src /app/src 
COPY test /app/test
COPY Makefile /app
EXPOSE 5000


#
# Production image
#

FROM base AS production
COPY src /app/src
COPY --from=development /app/requirements.txt ./
RUN pip install --no-cache-dir -r /app/requirements.txt \
    && rm /app/requirements.txt
EXPOSE 5000
