FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk update && \
  apk add --no-cache py-pip python-dev musl-dev gcc mariadb-dev && \
  pip install --no-cache-dir -r requirements.txt

#RUN apk del .build-deps python-dev musl-dev gcc mariadb-dev zlib-dev openssl-dev
#RUN rm -Rf ~/.cache

COPY . .

CMD ["gunicorn", "-b", ":8000", "-w", "4", "homepage.wsgi"]
