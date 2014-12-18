"""
WSGI config for homepage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import dotenv

try:
    dotenv.load_dotenv('.env')
except:
    pass


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homepage.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")
application = get_wsgi_application()
