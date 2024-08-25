# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get install -y tdsodbc
RUN apt-get install -y unixodbc
#RUN apt-get install -y unixodbc-dev

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-c", "/code/config/gunicorn.conf.py", "Sif.wsgi"]