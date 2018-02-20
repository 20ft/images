FROM alpine
RUN apk update ; apk upgrade
RUN apk add python3-dev zlib-dev jpeg-dev gcc musl-dev linux-headers postgresql-dev nginx
RUN pip3 install mezzanine psycopg2 gunicorn
