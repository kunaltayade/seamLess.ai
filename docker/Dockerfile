# Use official Python image
FROM python:3.13-slim

WORKDIR /app

COPY ../service/microservice.py ./
COPY ../service/hello.py ./
COPY ../requirements.txt ./

RUN pip install --no-cache-dir -r ../requirements.txt

EXPOSE 5000

CMD ["python", "microservice.py"]
