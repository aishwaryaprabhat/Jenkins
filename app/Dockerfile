FROM python:3.6
MAINTAINER aish, aish.prabhat@shopee.com
COPY requirements.txt bike/
WORKDIR bike/
RUN pip install -r requirements.txt
COPY api.py api.py
WORKDIR api/
EXPOSE 5000
CMD gunicorn wsgi:app