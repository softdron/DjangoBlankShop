import os

from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoblankshop.settings')
app = Celery('shop', broker='pyamqp://user:bitnami@django_rabbitmq_1:5672//')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)




