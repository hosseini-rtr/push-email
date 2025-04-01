import csv
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .forms import NewsletterForm
from .tasks import send_newsletter_email_task


class NewsletterUploadView(FormView):
    template_name = "upload_csv.html"
    form_class = NewsletterForm

    def form_valid(self, form):

        csv_file = form.cleaned_data["csv_file"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]

        decoded_file = csv_file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(decoded_file)

        if "email" not in reader.fieldnames or "name" not in reader.fieldnames:
            return HttpResponse("CSV must have 'email' and 'name' columns", status=400)

        for row in reader:
            email = row["email"]
            name = row["name"]
            send_newsletter_email_task.delay(email, name, subject, message)

        return HttpResponse("Emails are being sent in the background!")
