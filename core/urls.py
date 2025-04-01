from django.contrib import admin
from django.urls import path
from email_notify.views import MessageEmailView
from newsletter_notify.views import NewsletterUploadView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("email/", MessageEmailView.as_view(), name="Email form"),
    path("newsletter/", NewsletterUploadView.as_view(), name="Email form"),
]
