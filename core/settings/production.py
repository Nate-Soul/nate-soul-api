from .base import *

ALLOWED_HOSTS = [".vercel.app"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB_NAME"),
        'HOST': os.environ.get("POSTGRES_DB_HOST"),
        'PORT': os.environ.get("POSTGRES_DB_PORT"),
        'USER': os.environ.get("POSTGRES_DB_USER"),
        'PASSWORD': os.environ.get("POSTGRES_DB_PASS"),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

CORS_ALLOWED_ORIGINS = [
    "natesoulapi.vercel.app",
]