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

- Python 3.11+
- Django 5.x
- Celery 5.x
- RabbitMQ (installed and running)
- A virtual environment (recommended)

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd push-email
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install RabbitMQ**

   - On Ubuntu:
     ```bash
     sudo apt-get install rabbitmq-server
     sudo systemctl enable rabbitmq-server
     sudo systemctl start rabbitmq-server
     ```
   - On Mac:
     `bash
     brew install rabbitmq
     rabbitmq-server -detached
     `
     5.1. **Configure Settings**
     Make `core/settings.py` from `core/settings.py.sample` and replace SECRET_KEY:

   ```bash
   cp core/settings.py.sample core/settings.py
   ```

If forget how make a SECRET_KEY:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

5.2. **Configure Settings**
Update `core/settings.py` with your email backend settings:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

6. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

8. **Start Celery Worker**
   In a separate terminal:
   ```bash
   celery -A core worker -l info
   ```

## Usage

- **Individual Email**: Visit `/message/` to submit a form and send an email.
- **Newsletter**: Visit `/newsletter/` to upload a CSV file and send bulk emails.
  - CSV Format:
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

## Dependencies

- `django`: Web framework
- `celery`: Asynchronous task queue
- `celery[rabbitmq]`: RabbitMQ support for Celery
- `bootstrap`: Frontend styling (via CDN)

## TODO: RESTful API Development

Here are planned tasks to extend the project with RESTful APIs using Django REST Framework (DRF):

- [ ] **Install DRF**:

  - Add `rest_framework` to `INSTALLED_APPS` and install it via `pip install djangorestframework`.

- [ ] **Message API**:

  - Create a serializer for `MessageForm` data.
  - Build an endpoint (`/api/messages/`) to accept POST requests with `name`, `email`, and `message`.
  - Trigger `send_message_email_task` asynchronously on successful POST.

- [ ] **Newsletter API**:

  - Create a serializer for CSV upload and newsletter data.
  - Build an endpoint (`/api/newsletters/`) to accept POST requests with a CSV file, `subject`, and `message`.
  - Process the CSV and trigger `send_newsletter_email_task` for each row.

- [ ] **Authentication**:

  - Add token-based authentication (e.g., DRF's `TokenAuthentication`).
  - Restrict API access to authenticated users.

- [ ] **Rate Limiting**:

  - Implement rate limiting on API endpoints using DRF's throttling.

- [ ] **Documentation**:

  - Use DRF's built-in API documentation (e.g., Swagger/OpenAPI) with `drf-yasg`.

- [ ] **Testing**:
  - Write unit tests for API endpoints using Django's `TestCase` and DRF's `APITestCase`.

## Contributing

Feel free to fork this repository, submit issues, or send pull requests. Any contributions are welcome!
