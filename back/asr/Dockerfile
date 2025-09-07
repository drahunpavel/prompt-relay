FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY back/asr/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY back/asr/ ./asr/

WORKDIR /app/asr

ENV PYTHONPATH=/app

EXPOSE 8001

CMD ["python", "-m", "asr.main"]