# Push Emⓐil Project 📧

A Django-based application for sending emails asynchronously using Celery and RabbitMQ. This project includes features for sending individual messages via a form and bulk email newsletters using CSV uploads.

## Features

- **Individual Email Sending**: Users can submit a form with their name, email, and message to send an email asynchronously.
- **Bulk Newsletter Sending**: Upload a CSV file with `email` and `name` columns to send personalized newsletters to multiple recipients.
- **Asynchronous Processing**: Uses Celery with RabbitMQ as the message broker to handle email sending in the background.
- **Responsive UI**: Built with Bootstrap for a clean and user-friendly interface.

## Project Structure

```
push-email/
├── core/                  # Core settings and Celery configuration
│   ├── celery.py
│   └── settings.py
├── email_notify/          # App for individual email sending
│   ├── templates/
│   ├── email.py
│   ├── forms.py
│   ├── tasks.py
│   └── views.py
├── newsletter_notify/     # App for bulk newsletter sending
│   ├── templates/
│   ├── forms.py
│   ├── tasks.py
│   └── views.py
├── static/                # Static files (CSS, JS, etc.)
└── templates/             # Base templates
    └── base.html
```

## Prerequisites

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
    email,name
    example1@gmail.com,John
    example2@gmail.com,Jane
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
