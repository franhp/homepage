"""
Django settings for homepage project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join, normpath, dirname

from configurations import Configuration, values
import debug_toolbar
import dotenv


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)
    ALLOWED_HOSTS = []
    
    # Application definition
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Internal
        'links',
        'myplaces',
        'tvseries',
        
        # Extra
        'django_extensions',
        'rest_framework',
        'geoposition',
        'ajax_select',
        'compressor'
    )

    MIDDLEWARE_CLASSES = (
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'homepage.urls'
    WSGI_APPLICATION = 'homepage.wsgi.application'
    
    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.7/topics/i18n/
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = normpath(join(BASE_DIR, 'static'))
    STATICFILES_FINDERS = (
               'django.contrib.staticfiles.finders.FileSystemFinder',
               'django.contrib.staticfiles.finders.AppDirectoriesFinder',
               'compressor.finders.CompressorFinder')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = normpath(join(BASE_DIR, 'media'))
    
    # Templates
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        normpath(join(BASE_DIR, 'templates')),
    )
    
    # Compressors
    # COMPRESS_PRECOMPILERS = (
    #    ('text/scss', 'sass --scss --compass {infile} {outfile}'),
    # )

    # Ajax admin
    AJAX_LOOKUP_CHANNELS = {
        'tvserieschannel': ('tvseries.lookups', 'TVSeriesLookup')
    }
    
    # API keys
    dotenv.read_dotenv()
    LASTFM_KEY = os.environ.setdefault('LASTFM_KEY', None)
    TWITTER_CLIENT_KEY = os.environ.setdefault('TWITTER_CLIENT_KEY', None)
    TWITTER_CLIENT_SECRET = os.environ.setdefault('TWITTER_CLIENT_SECRET', None)


class Development(Common):
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []
    INSTALLED_APPS = Common.INSTALLED_APPS + ('debug_toolbar',)
    
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + (
          'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    
    INTERNAL_IPS = ('127.0.0.1',)

    TEMPLATE_DIRS = Common.TEMPLATE_DIRS + \
                    (join(dirname(debug_toolbar.__file__), 'templates'),)
    STATICFILES_DIRS = Common.STATICFILES_DIRS + \
                    (join(dirname(debug_toolbar.__file__), 'static'),)
    
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
