FROM python:3.13-slim

WORKDIR /app

RUN apt-get update

COPY back/bot/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY back/bot/ ./bot/

WORKDIR /app/bot

ENV PYTHONPATH=/app

CMD ["python", "-m", "bot.main"]