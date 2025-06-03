# 1. Python imidjini olamiz
FROM python:3.11-slim

# 2. Uzbushundagi muhit
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Ish papkasi
WORKDIR /code

# 4. OS paketlari (Postgres dev, gcc kerak bo‘lsa)
RUN apt-get update \
 && apt-get install -y build-essential libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# 5. Talabnomalarni nusxalab, o‘rnatamiz
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Kodni konteynerga nusxalaymiz
COPY . /code/

# 7. Static to‘plash (prod ko‘tarish uchun)
RUN python manage.py collectstatic --noinput

# 8. Default run — Daphne ASGI server
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "config.asgi:application"]
