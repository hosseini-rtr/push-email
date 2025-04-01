from email_notify.forms import MessageForm
from django.views.generic.edit import FormView
from django.http import HttpResponse


class MessageEmailView(FormView):
    template_name = "message.html"
    form_class = MessageForm

    def form_valid(self, form):
        form.send_email()
        return HttpResponse("Email sent successfully")
