import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video_subtitle.settings')
app = Celery('video_subtitle')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()