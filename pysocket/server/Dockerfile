FROM python:3.8-slim-buster

WORKDIR /app

COPY server.py .
ENV PORT=8080

CMD [ "python3", "-u", "server.py"]