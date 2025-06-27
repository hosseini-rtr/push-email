from celery import shared_task
from celery.utils.log import get_task_logger

from .email import send_message_email

logger = get_task_logger(__name__)


@shared_task(name="send_message_email_task")
def send_message_email_task(name, email, message):
    logger.info("Sent message email")
    logger.info(f"content: {name, email, message}")
    return send_message_email(name, email, message)
