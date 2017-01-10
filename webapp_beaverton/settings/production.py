import os
from webapp_beaverton.settings.export_env import set_env
from webapp_beaverton.settings.base import *

# initialize environment variable
set_env("production")


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USERNAME'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['HOST'],
        'PORT': os.environ['PORT'],
    }
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# INSTALLED_APPS += (
#     # other apps for production site
# )
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = 'Aglean <' + os.environ['EMAIL_HOST_USER'] + '>'
