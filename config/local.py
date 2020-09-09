from config.base import *
import os
import logging

logger = logging.getLogger(__name__)


msg = "Running in LOCAL CONFIGURATION. Version: {0}".format(os.environ.get("FORESIDE_VERSION",""))
print(msg)
logger.info(msg)

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

