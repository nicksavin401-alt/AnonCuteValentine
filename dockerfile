FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1) зависимости отдельно (для кэша слоёв)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) копируем код
COPY bot /app/bot

# 3) пользователь и директория под данные (sqlite, файлы и т.п.)
RUN useradd -m -u 1000 appuser \
    && mkdir -p /app/data \
    && chown -R appuser:appuser /app

USER appuser

CMD ["python", "bot/main.py"]
