FROM python:3.12-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt -y install cron nano

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

COPY ./cron /etc/cron.d/cron

RUN chmod 0644 /etc/cron.d/cron
RUN crontab /etc/cron.d/cron

EXPOSE 8000

CMD sh -c "cron && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
