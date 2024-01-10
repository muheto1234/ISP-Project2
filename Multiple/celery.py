import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Multiple.settings')

app = Celery('nom_du_projet')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()