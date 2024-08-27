"""
Django settings for Sif project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import logging
import sys
import random
#import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SIF_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ['SIF_IN_PROD'] == 1:
    DEBUG = False
else:
    DEBUG = True
    print('DEBUG IS ON')

#DEBUG = False

#APPEND_SLASH = False

ALLOWED_HOSTS = ['127.0.0.1',
                 'sif-django-backend-fhh0.onrender.com',
                 'sif-vue-frontend-6xh9.onrender.com',
                 'sif-dev-frontend.onrender.com',
                 'sif-dev-backend.onrender.com',
                 'sif.fri.is',
                 'fri.is']

CORS_ALLOWED_ORIGINS = [
    "https://sif-django-backend-fhh0.onrender.com",
    "https://sif-vue-frontend-6xh9.onrender.com",
    "https://sif-dev-frontend.onrender.com",
    "https://sif-dev-backend.onrender.com",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://sif.fri.is"
]


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    'corsheaders',
    'django.contrib.staticfiles',
    'Sif',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Sif.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [ os.path.join(BASE_DIR, 'templates/') ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 #'django.contrib.auth.context_processors.auth',
#                 #'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'Sif.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Database settings for the MS-SQL server. We use the django-mssql package for this.
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ['SIF_DB_NAME'],
        'HOST': os.environ['SIF_DB_HOST'],
        'PORT': os.environ['SIF_DB_PORT'],
        'USER': os.environ['SIF_DB_USER'],
        'PASSWORD': os.environ['SIF_DB_PASSWORD'],
        'OPTIONS': {
            'driver': os.path.join(BASE_DIR, '/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so'), # The driver is installed on Heroku using the Aptfile into this path.
            'host_is_server': True,
        },
    },
    #'competitor_list': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
}

if os.environ['SIF_IN_PROD'] == 1:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "KEY_PREFIX:": "prod", # Prefix for the keys in the cache to separate production and development
            "VERSION": 1,
            "LOCATION": os.environ['SIF_REDIS_URL'],
        }
    }
else:
    if 'SIF_ON_RENDER' in os.environ:
        CACHES = {
            "default": {
                "BACKEND": "django.core.cache.backends.redis.RedisCache",
                "KEY_PREFIX:": "dev", # Prefix for the keys in the cache to separate production and development
                "VERSION": random.randint(1, 1000), # Random version to avoid cache collisions, we don't flush the cache on every deploy for development
                "LOCATION": os.environ['SIF_REDIS_URL'],
            }
        }
    else:
        CACHES = {
            "default": {
                "BACKEND": "django.core.cache.backends.dummy.DummyCache",
            }
        }

# if 'SIF_ON_HEROKU' in os.environ:
#     CACHES = {'default': {
#         'BACKEND': 'django_bmemcached.memcached.BMemcached',
#         'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
#         'OPTIONS': {
#                     'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
#                     'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD'),
#             }
#         }
#     }
# else:
#     CACHES = {
#         'default': {
#             'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#         }
#     }

# # Logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
#                        'pathname=%(pathname)s lineno=%(lineno)s '
#                        'funcname=%(funcName)s %(message)s'),
#             'datefmt': '%Y-%m-%d %H:%M:%S'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         }
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#     }
# }

LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'formatters': {
       'verbose': {
           'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
       },
   },
   'handlers': {
       'console': {
           'level': 'INFO',
           'class': 'logging.StreamHandler',
           'stream': sys.stdout,
           'formatter': 'verbose'
       },
   },
   'loggers': {
       '': {
           'handlers': ['console'],
           'level': 'INFO',
           'propagate': True,
       },
   },
}

#MIGRATION_MODULES = {
#    'auth': None
#}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Force HTTPS if on Render
if 'SIF_ON_RENDER' in os.environ:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

# Disable admin panel
ADMIN_ENABLED = False


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'is'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#STATIC_URL = '/staticfiles/'
#STATIC_URL = '/staticfiles/'

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'staticfiles'),
#)

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    STATIC_URL = '/staticfiles/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'staticfiles'),
    )

# Activate Django-Heroku. We have our own database settings and we set the private key ourselves.
#django_heroku.settings(locals(), databases=False, secret_key=False, logging=False, staticfiles=False)
