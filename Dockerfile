FROM python:3.10
RUN mkdir /app
COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app/src
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app
EXPOSE 8000
