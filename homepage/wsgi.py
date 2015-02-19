"""
WSGI config for homepage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import dotenv
dotenv.read_dotenv()

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
