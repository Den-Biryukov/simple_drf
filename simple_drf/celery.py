import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_drf.settings')

app = Celery('simple_drf')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'send-mail-everyday-minute': {
        'task': 'app.tasks.send_beat_mail',
        'schedule': crontab(hour='*/1'),
    },
}
