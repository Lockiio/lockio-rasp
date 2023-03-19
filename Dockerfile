FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt /app
COPY ./lockio-rasp /app/lockio-rasp
RUN pip install -r requirements.txt

EXPOSE 8080

ENV FLASK_RUN_PORT=8001
ENV FLASK_APP=lockio-rasp/app.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8001"]