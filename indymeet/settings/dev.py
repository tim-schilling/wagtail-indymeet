# ----------------------------------------------
# For developing locally
# ----------------------------------------------
from __future__ import annotations

from .base import *  # noqa F403 F401

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-b$)hky-=v&f&48g-dtnehezmj$w4%e+in*oe*!r=kh4n4+k0sg"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

BASE_URL = "http://localhost:8000"

RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

try:
    from .local import *  # noqa F403 F401
except ImportError:
    pass
