FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get -y update && \
  apt-get -y install python3-dev build-essential && \
  pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", ":8000", "-w", "4", "homepage.wsgi"]
