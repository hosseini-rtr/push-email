# newsletter_notify/forms.py
from django import forms


class NewsletterForm(forms.Form):
    csv_file = forms.FileField(
        label="CSV File",
        help_text="Upload a CSV file with columns: email, name",
    )
    subject = forms.CharField(
        label="Subject",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
    )
