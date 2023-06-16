"""
Django settings for CardsMaker project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.template.context_processors import static
from django_countries import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*b@l20(s5&8kv^ng@gadbvvz+h06jy=m32&@#+$^n))x%l&c!%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*","10.0.2.2","192.168.43.216","localhost"]


# Application definition


sys.modules['fontawesome_free'] = __import__('fontawesome-free')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fontawesomefree',
    'languages',
    'users',
    'biodata',
    'wedding_cards',
    'engagement_cards',
    'bussiness_cards',
    'wkhtmltopdf',
    'cities_light',
    'mathfilters',
    'resume',
    'latter_had',
    'agora',

    'qr_code',
]

MIDDLEWARE = [
    # 'CardsMaker.middleware.SameSiteMiddleware',  # position it at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CardsMaker.urls'
# SESSION_COOKIE_SAMESITE = None
# CSRF_COOKIE_SAMESITE = None
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SESSION_SAVE_EVERY_REQUEST = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'templatetags': 'users.templatetags.templatetags',
            },
        },

    },
]

WSGI_APPLICATION = 'CardsMaker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
TESTING_MODE = False
if TESTING_MODE == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "myproject",
            'USER': 'myprojectuser',
            'PASSWORD': 'Hari2228@',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static'
# Extra lookup directories for collectstatic to find static files
STATIC_URL = '/assets/'
MEDIA_URL = 'media/'
# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (os.path.join(str(BASE_DIR)+"/static/"),)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')
APPEND_SLASH = False
if DEBUG:
    RAZOR_KEY_ID = "rzp_test_pRwByYGHjIP0t2"
    RAZOR_KEY_SECRET = "GOfSmvSm0jAlTiwiBoXue8kP"
else:
    RAZOR_KEY_ID = "H2K22dD1I3soH9"
    RAZOR_KEY_SECRET = "rzp_test_7nruGgj5EfDxGO"

LOGIN_REDIRECT_URL = '/'