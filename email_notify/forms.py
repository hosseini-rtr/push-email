from django import forms
from .tasks import send_message_email_task


class MessageForm(forms.Form):

    name = forms.CharField(
        label="FirstName",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "First Name",
                "id": "form-firstname",
            }
        ),
    )

    email_address = forms.EmailField(
        label="Email",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "E-mail",
                "id": "form-email",
            }
        ),
    )

    message = forms.CharField(
        label="message",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Your message",
                "rows": "5",
                "id": "form-message",
            }
        ),
    )

    def send_email(self):
        send_message_email_task.delay(
            self.cleaned_data["name"],
            self.cleaned_data["email_address"],
            self.cleaned_data["message"],
        )
