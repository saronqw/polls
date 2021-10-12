FROM python:3.10-alpine

# set work directory
WORKDIR /usr/src/app

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .


RUN python manage.py collectstatic

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]