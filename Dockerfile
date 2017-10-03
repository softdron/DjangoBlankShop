FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
#RUN django-admin startapp shop
#RUN python manage.py startapp cart
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
