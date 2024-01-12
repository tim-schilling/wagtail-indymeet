from __future__ import annotations

from .base import *

DEBUG = False
ALLOWED_HOSTS = [os.environ["VIRTUAL_HOST"]]

EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
MAILJET_API_KEY = os.getenv("MAILJET_API_KEY")
MAILJET_SECRET_KEY = os.getenv("MAILJET_SECRET_KEY")
ANYMAIL = {
    "MAILJET_API_KEY": MAILJET_API_KEY,
    "MAILJET_SECRET_KEY": MAILJET_SECRET_KEY,
}
BASE_URL = os.getenv("BASE_URL", "https://djangonaut.space")
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")
STATICFILES_DIRS += [
    os.path.join(BASE_DIR, "theme", "static"),
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ["DB_HOST"],
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "OPTIONS": {
            "client_encoding": "UTF8",
            "sslmode": os.environ.get("DB_SSLMODE", "require"),
        },
    }
}

WAGTAILADMIN_BASE_URL = f"http://{os.environ['VIRTUAL_HOST']}"

# Add more logging for production.
try:
    # Attempt to create the file
    with open("/var/log/django.log", "x") as file:
        pass  # No action needed, just creating the file
except FileExistsError:
    # File already exists, configure the file logging.
    LOGGING["root"] = {"level": "WARNING", "handlers": ["console", "file"]}
    LOGGING["handlers"]["file"] = {
        "class": "logging.handlers.TimedRotatingFileHandler",
        "filename": "/var/log/django.log",
        "formatter": "verbose",
        "filters": ["require_debug_false"],
        "when": "midnight",
        "backupCount": 10,
    }
    LOGGING["loggers"]["django"] = {
        "handlers": ["file"],
        "level": "INFO",
        "propagate": True,
    }
except PermissionError:
    # Can't create the file so don't instrument the file logger
    pass
