from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_message_email(name, email, message):
    context = {
        "name": name,
        "email": email,
        "message": message,
    }

    print("context", context)

    email_subject = "Thank you form your message"
    email_body = render_to_string("email_message.txt", context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [
            email,
        ],
    )
    return email.send(fail_silently=False)
