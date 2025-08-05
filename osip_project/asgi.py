"""
ASGI config for osip_project project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osip_project.settings')

application = get_asgi_application()
