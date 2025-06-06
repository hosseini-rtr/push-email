from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage
from django.conf import settings

logger = get_task_logger(__name__)

@shared_task(name="send_newsletter_email_task")
def send_newsletter_email_task(email, name, subject, message):
    email_body = f"Hello {name},\n\n{message}"
    email = EmailMessage(
        subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )
    logger.info(f"Sending email to {email}")
    return email.send(fail_silently=False)