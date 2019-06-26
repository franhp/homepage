FROM node:10
COPY static/ static/
COPY package.json .
RUN npm i && npm run sass


FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get -y update && \
  apt-get -y install python3-dev build-essential && \
  pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ["/usr/src/app/static/"]
COPY --from=0 static/COMPILED/css/* static/COMPILED/css/
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "-b", ":8000", "-w", "4", "homepage.wsgi"]
