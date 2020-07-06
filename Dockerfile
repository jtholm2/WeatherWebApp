FROM ubuntu:latest
EXPOSE 2222
RUN apt-get update
RUN apt-get install -y python3
ADD . /weather_by_zipcode
WORKDIR /weather_by_zipcode
RUN apt install -y virtualenv
RUN virtualenv --python=python3 env
RUN . env/bin/activate &&\
    pip install django &&\
    pip install requests
CMD . env/bin/activate && python manage.py runserver

