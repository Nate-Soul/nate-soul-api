from .base import *

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get("POSTGRES_DB_NAME"),
#         'HOST': os.environ.get("POSTGRES_DB_HOST"),
#         'PORT': os.environ.get("POSTGRES_DB_PORT"),
#         'USER': os.environ.get("POSTGRES_DB_USER"),
#         'PASSWORD': os.environ.get("POSTGRES_DB_PASS"),
#     }
# }

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]