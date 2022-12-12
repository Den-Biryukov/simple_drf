from simple_drf.celery import app
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from simple_drf import settings


@app.task(bind=True)
def send_beat_mail(self):
    users = get_user_model().objects.all()
    mail_subject = "spam"
    for user in users:
        send_mail(
            subject=mail_subject,
            message=f'Dear {user.username}, Hello!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=True,
        )

    return f"email was sent to users"
