FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

# copy project
COPY . /code/

RUN rm -f .env
RUN mkdir -p /code/static

RUN apk update && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev && \
    pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /code/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

CMD python manage.py runserver 0.0.0.0:8000