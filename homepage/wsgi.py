"""
WSGI config for homepage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import sys
import os

vendor_libs_path = os.path.join(os.getcwd(), 'lib')
if os.path.exists(vendor_libs_path):
    sys.path.insert(0, vendor_libs_path)

import dotenv
dotenv.read_dotenv()

from dj_static import Cling
from configurations.wsgi import get_wsgi_application
application = Cling(get_wsgi_application())