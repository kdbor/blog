# Base build
FROM python:3.10-alpine as base

ENV WORKDIR=/usr/app

# set work directory
WORKDIR $WORKDIR
RUN apk add --update --virtual .build-deps \
    build-base \
    postgresql-dev \
    python3-dev \
    libpq

RUN apk add libffi-dev

COPY requirements.txt $WORKDIR/requirements.txt
RUN pip install -r $WORKDIR/requirements.txt

# Now multistage build
FROM python:3.10-alpine

ENV WORKDIR=/usr/app

# set work directory
WORKDIR $WORKDIR

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add libpq
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

# copy project
COPY . $WORKDIR

CMD ["gunicorn", "--preload"]