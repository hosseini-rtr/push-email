# Django Notification Apps Project

This project contains a Django example (`core`) and two reusable Django applications:
- **Email Notify (`django-email-notify`)**: For handling email notifications.
- **Newsletter Notify (`django-newsletter-notify`)**: For managing newsletter functionalities.

## Project Structure

- `core/`: A Django project that demonstrates how to use the notification apps.
- `packages/`: Contains the individual, installable Django apps.
    - `email_notify_pkg/`: Contains the `django-email-notify` app and its packaging files.
    - `newsletter_notify_pkg/`: Contains the `django-newsletter-notify` app and its packaging files.
- `manage.py`: Django's command-line utility for the `core` project.
- `requirements.txt`: Specifies dependencies for the main project and the local packages.

## Getting Started

1.  Clone the repository.
2.  Create and activate a virtual environment.
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    This will also install `django-email-notify` and `django-newsletter-notify` in editable mode.
4.  Set up the Django project:
    - Copy `core/settings.py.sample` to `core/settings.py`.
    - Update `core/settings.py` with your database settings, secret key, email configurations, etc.
5.  Run migrations:
    ```bash
    python manage.py migrate
    ```
6.  Run the development server:
    ```bash
    python manage.py runserver
    ```

Refer to the README files within each app's directory in `packages/` for more detailed information on using them.
