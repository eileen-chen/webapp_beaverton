import os
from webapp_beaverton.settings.export_env import set_env
from webapp_beaverton.settings.base import *

# initialize environment variable
set_env("development")

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USERNAME'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

# INSTALLED_APPS += (
#     'debug_toolbar', # and other apps for local development
# )

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = 'Aglean <' + os.environ['EMAIL_HOST_USER'] + '>'

