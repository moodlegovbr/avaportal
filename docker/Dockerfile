FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add gcc python3-dev musl-dev postgresql-dev jpeg-dev zlib-dev libffi-dev && \
    apk add postgresql-libs py3-cffi libjpeg && \
    pip install psycopg2-binary pillow social-auth-app-django && \
    apk --purge del gcc python3-dev musl-dev postgresql-dev jpeg-dev zlib-dev libffi-dev

ADD install_packages.sh .
ADD startup.sh .

ADD requirements.txt . 
RUN pip install -r /requirements.txt

WORKDIR /apps/app
CMD /startup.sh
