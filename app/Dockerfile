FROM python:3.11.1-bullseye
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
RUN mkdir -p /app/sbudget/static

WORKDIR /app
RUN apt-get update && \
    apt-get install -y locales && \
    apt-get install -y python-dev python3-dev libldap2-dev libsasl2-dev libssl-dev netcat-openbsd poppler-utils && \
    echo ru_RU.UTF-8 UTF-8 >> /etc/locale.gen && \
    locale-gen && \
    python -m pip install poetry && \
    poetry config virtualenvs.create false && \
    rm -rf /var/lib/apt/lists/* && rm -rf /etc/apk/cache
COPY pyproject.toml poetry.lock ./
RUN python -m pip install --upgrade pip && \
    poetry self update && \
    poetry install --no-root
COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 80
