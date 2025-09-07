FROM python:3.13-slim

WORKDIR /app

RUN apt-get update

COPY back/api/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY back/api/ ./api/

WORKDIR /app/api

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["python", "-m", "api.main"]