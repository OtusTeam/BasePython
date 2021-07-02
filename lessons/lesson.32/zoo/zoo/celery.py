import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoo.settings')
celery_app = Celery('zoo')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()