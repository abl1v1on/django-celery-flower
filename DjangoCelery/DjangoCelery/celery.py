import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoCelery.settings')

app = Celery('DjangoCelery')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое подцепление тасков
app.autodiscover_tasks()


