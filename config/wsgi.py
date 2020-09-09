"""
WSGI config for foreside project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


ENV = os.environ.get('ENV', None)
if ENV and ENV.upper() == 'LOCAL':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.local')
else:
    raise Exception('Environment is not set. export ENV=[local or prod or dev]')

application = get_wsgi_application()
