FROM python:alpine3.20

WORKDIR /usr/app/src/

COPY server.py .
COPY index.html .

EXPOSE 3000

ENV PYTHONUNBUFFERED=1

CMD ["python", "./server.py"]