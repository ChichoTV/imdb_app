FROM python:3.8.5-slim-buster
ENV INSTALL_PATH /imdb
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "imdb.app:create_app()"