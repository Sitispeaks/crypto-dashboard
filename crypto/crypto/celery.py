from __future__ import absolute_import ,unicode_literals
import os
from celery import Celery
from django.conf import settings
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto.settings')
# os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app=Celery('crypto')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object('django.conf:settings',namespace='CELERY')

#celery beat settings
app.conf.beat_schedule={
    'get_coins_data_at_every_30s': {
        'task':'coins.tasks.get_coins_data',
        'schedule': 30.0,
    },
}

app.autodiscover_tasks()

@app.task()
def debug_task(self, task):
    print(f'Request: {self.request!r}')
