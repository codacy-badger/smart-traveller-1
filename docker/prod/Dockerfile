FROM python:3.8-alpine

LABEL application='smarttraveller'

LABEL maintainer='Anyama Richard'

WORKDIR /app

# update system and install dependencies
RUN apk update && apk add --no-cache bash \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2==2.8.4 \
    && apk del build-deps \
    && pip install pipenv gunicorn

#copy source code to app dir
COPY smarttravellersapi/ /app/
ADD Pipfile /app/

ADD scripts/prod_start.sh /app/

# add execute permission
RUN chmod +x prod_start.sh

# install app dependencies from the pipfile
RUN pipenv install --skip-lock --system && \
    apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev \
    libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

CMD bash -c "source prod_start.sh"

