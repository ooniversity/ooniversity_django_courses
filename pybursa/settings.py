# -*- coding: utf-8 -*-
"""
Django settings for pybursa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y0$c2tm4q941$$iv3b^7308_d7ye+qj3z1%4bm5-9xsf=0g*49'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'quadratic',
    'courses',
    'students',
    'coaches',
    'mails',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025
#EMAIL_HOST_USER = 'NikolayBorovenskiy'
# EMAIL_HOST_PASSWORD = 'acmilan'

#EMAIL_BACKEND = "sgbackend.SendGridBackend"
#SENDGRID_USER = "NikolayBorovenskiy"
#SENDGRID_PASSWORD = "acmilan"
#Send email with service send grid
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'NikolayB'
EMAIL_HOST_PASSWORD = 'acmilan86'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ADMINS = (('Nikolay', 'nikolay.borovenskiy@gmail.com'), ('Sasha', 'sasha_tep@mail.ru'))

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'student': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
    },
    'loggers':
    {
        'courses': {
            'handlers': ['file_course'],
            'level': 'DEBUG',
        },
        'students': {
            'handlers': ['file_student'],
            'level': 'DEBUG',
        },
    },
    'handlers':
    {
        'file_course': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug_course_detail.log'),
            'formatter': 'simple'
        },
        'file_student': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug_student_detail.log'),
            'formatter': 'student'
        },
    },

}
