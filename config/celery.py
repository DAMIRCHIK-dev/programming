import os
from celery import Celery

# Django sozlamalarini yuklaymiz
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

# Settings ichidagi CELERY_ prefiksli sozlamalarni yuklash
app.config_from_object("django.conf:settings", namespace="CELERY")

# Har bir app ichidagi tasks.py ni avtomatik aniqlash
app.autodiscover_tasks()
