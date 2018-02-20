"""
Django settings for VulgaireDev project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import sys
import os

import requests_cache

sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("VULGAIREDEV_SECRET_KEY", '')
VULGAIREDEV_DB_PASSWORD = os.environ.get("VULGAIREDEV_DB_PASSWORD", '')
VULGAIREDEV_GMAIL_PASSWORD = os.environ.get("VULGAIREDEV_DB_PASSWORD", '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

ALLOWED_HOSTS = ['www.vulgairedev.fr',
                 '.vulgairedev.fr', '127.0.0.1', 'localhost', 'web']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'VulgaireDev.templatetags',
    'VulgaireDev',
    'blog',
    'disqus',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'VulgaireDev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'VulgaireDev.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vulgairedev',
        'USER': 'vulgairedev',
        'PASSWORD': VULGAIREDEV_DB_PASSWORD,
        'HOST': 'db',
        'PORT': '',
    }
}

# Request cache
requests_cache.install_cache(cache_name='github_cache', backend='sqlite',
                             expire_after=120)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# mails
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vulgairedev@gmail.com '
EMAIL_HOST_PASSWORD = VULGAIREDEV_GMAIL_PASSWORD

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ''

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOGIN_URL = '/connexion/'


DISQUS_API_KEY = os.environ.get("DISQUS_KEY", '')
DISQUS_WEBSITE_SHORTNAME = 'VulgaireDev'

SITE_ID = 1
