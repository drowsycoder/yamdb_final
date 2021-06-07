FROM python:3.8.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/code
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR APP_HOME

# For installing Psycopg2 in an Alpine-based Docker Image
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
COPY . .

ENTRYPOINT ["entrypoint.sh"]

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000