FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       default-libmysqlclient-dev \
       pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=videoconferencing.settings

CMD ["gunicorn", "--timeout", "120", "--bind", "0.0.0.0:8000", "videoconferencing.wsgi:application"]