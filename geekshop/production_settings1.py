import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'NAME': 'geekshop',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'django',
        'PASSWORD': 'geekbrains',
        'HOST': 'localhost'
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
