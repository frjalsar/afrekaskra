"""
Django settings for Sif project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SIF_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if 'SIF_ON_HEROKU' in os.environ:
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = [] # The django_heroku package takes care of this.


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    'Sif',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Sif.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates/') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #'django.contrib.auth.context_processors.auth',
                #'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Sif.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Database settings for the MS-SQL server. We use the django-mssql-backend package for this.
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'Athletics',
        'HOST': '82.221.94.225',
        'USER': os.environ['SIF_DB_USER'],
        'PASSWORD': os.environ['SIF_DB_PASSWORD'],

        'OPTIONS': {
            #'driver': '/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.4.so.2.1',
            'driver': os.path.join(BASE_DIR, 'drv/msodbcsql17/lib64/libmsodbcsql-17.5.so.2.1'), # The driver is in the GIT repository
            'host_is_server': True,
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

# Disable admin panel
ADMIN_ENABLED = False


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'is'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#STATIC_URL = '/staticfiles/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Activate Django-Heroku. We have our own database settings and we set the private key ourselves.
django_heroku.settings(locals(), databases=False, secret_key=False)

