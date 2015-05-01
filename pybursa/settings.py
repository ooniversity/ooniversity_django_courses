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
SECRET_KEY = 'y(07otd)p!+f)x91!1mdwmm@g-mh#47v)7xrkhdwnbh9%65=$r'

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
    'feedbacks',
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

LANGUAGE_CODE = 'ru-ru'  # 'en-us'

TIME_ZONE = None  # 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )


# Template files (HTML)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# EMAIL settings

EMAIL_HOST = 'localhost'

EMAIL_PORT = 1025

#EMAIL_HOST_USER = 'TeplovAlexander'

#EMAIL_HOST_PASSWORD = '123456'


ADMINS = (('Alexander', 'sasha_tep@mail.ru'),)


# Configuration logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # Loggers settings
    'loggers': {
        'courses': {
            'level': 'DEBUG',
            'handlers': ['null', 'console_course', 'file_course'],
            'propagate': True,
        },
        'students': {
            'level': 'WARNING',
            'handlers': ['console_student', 'file_student'],
            'propagate': True,
        }
    },

    # Handlers settings
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console_course': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_student': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        # Logging files for applications (courses and students)
        'file_course': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'courses/debug.log'),
            'formatter': 'simple'
        },
        'file_student': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students/debug.log'),
            'formatter': 'verbose'
        }
    },

    # Formatters using settings
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s in %(funcName)s - %(message)s'
        },
        'simple': {
            'format': '%(levelname)s - %(message)s'
        }
    }
}
