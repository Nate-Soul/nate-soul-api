from .base import *

ALLOWED_HOSTS = [".vercel.app"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'URL': '',
        'NAME': 'bluemall',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': '$xE)rkhop6A3jsl1PX',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

CORS_ALLOWED_ORIGINS = [
    "natesoulapi.vercel.app",
]