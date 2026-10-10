FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

COPY app.py .

EXPOSE 8080

USER nobody

CMD ["python", "app.py"]
