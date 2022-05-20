FROM python:3.8-slim-buster

WORKDIR /app

COPY client.py .
ENV HOST=pyserver
ENV PORT=8080

CMD [ "python3", "-u", "client.py"]