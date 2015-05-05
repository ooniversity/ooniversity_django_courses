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
SECRET_KEY = '6ipzxp*#$otep)vavohzb-cv5ok0v-r*ke@rmuk*v0j0l8gbui'

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
    'feedback',
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

TIME_ZONE = 'Europe/Kiev' # UTC--- Kyiv; by OPersian

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Debugging - by OPersian
LOGGING = {
    'version': 1,
    #'disable_existing_loggers': False,
    'loggers': {
        'courses': {
            'handlers': ['file_courses'],
            'level': 'DEBUG',
            #'propagate': True,
        },
        'students': {
            'handlers': ['file_students'],
            'level': 'WARNING',
        },
    },
    'handlers': {
        'file_courses': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            #'filename': '/path/to/django/debug.log',
            'filename': os.path.join(BASE_DIR, 'courses_debug.log'),
            'formatter': 'verbose_user_defined',
        },
        'file_students': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students_debug.log'),
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            #'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
        'verbose_user_defined': {
            'format': '%(levelname)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },


}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

#TEMPLATE_LOADERS = 
#('django.template.loaders.filesystem.Loader',
#'django.template.loaders.app_directories.Loader')

#AUTH_PROFILE_MODULE = 'coaches.Coach'

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
#EMAIL_HOST_USER = "OPersian"
#EMAIL_HOST_PASSWORD = "password"

#ADMINS = (('OPersian', 'olena.persianova@gmail.com'),)
ADMINS = ('olena.persianova@gmail.com',)
