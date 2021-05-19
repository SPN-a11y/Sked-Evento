"""
WSGI config for evento project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
>>>>>>> 510c6698a7363255e069857aaad21b8d12919ba7
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evento.settings')

application = get_wsgi_application()
