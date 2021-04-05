import os
import sys
from datetime import timedelta
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]

ADMINS = ()
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'qsessions',
    'django_rq',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',
    'users',
    'commands'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'qsessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

APPEND_SLASH = True

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
   ('en', _('English')),
   ('ar', _('Arabic')),
]

TIME_ZONE = 'Asia/Jerusalem'

USE_I18N = True

USE_L10N = False

USE_TZ = False

DATE_FORMAT = 'Y-m-d'
SHORT_DATE_FORMAT = 'Y-m-d'

DATETIME_FORMAT = 'Y-m-d H:i:s'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i:s'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '.static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
REDIS_EXPIRE_TIME = int(os.getenv('REDIS_EXPIRE_TIME', 60 * 60 * 24 * 30))
REDIS_DB = 0

# Caches
# in seconds
CACHE_TTL = 60 * 60 * 12
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'TIMEOUT': CACHE_TTL
    }
}

AXES_LOCK_OUT_AT_FAILURE = True
AXES_FAILURE_LIMIT = 5  # 5 failure attempts
AXES_COOLOFF_TIME = timedelta(minutes=15)  # locked for 15 min
AXES_RESET_ON_SUCCESS = True
AXES_LOCKOUT_URL = 'locked/'
AXES_PROXY_COUNT = 0


# IP middle ware
IPWARE_META_PRECEDENCE_ORDER = (
    'REMOTE_ADDR',
    'HTTP_X_FORWARDED_FOR', 'X_FORWARDED_FOR',
    'HTTP_CLIENT_IP',
    'HTTP_X_REAL_IP',
    'HTTP_X_FORWARDED',
    'HTTP_X_CLUSTER_CLIENT_IP',
    'HTTP_FORWARDED_FOR',
    'HTTP_FORWARDED',
    'HTTP_VIA',
)

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'users.User'
SESSION_ENGINE = 'qsessions.backends.cached_db'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'INFO',
        'handlers': ['info_file', 'mail_admins'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(filename)s %(funcName)s %(process)d %(thread)d %(threadName)s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', ],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': sys.stdout,
        },
        'rq_console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': sys.stdout,
        },
        'info_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': '/var/log/django/info.logs'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'info_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['info_file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null', ],
            'propagate': False,
        },
    },
}

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

RQ_SHOW_ADMIN_LINK = True


CACHE_TTL = 60 * 60 * 12

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'TIMEOUT': CACHE_TTL
    }
}

# RQ job
RQ_QUEUES = {
    'default': {
        'URL': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
        'DEFAULT_TIMEOUT': 500,
        'USE_REDIS_CACHE': 'default',
    },
    'high': {
        'URL': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
        'DEFAULT_TIMEOUT': 500,
        'USE_REDIS_CACHE': 'default',
    },
    'low': {
        'URL': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
        'DEFAULT_TIMEOUT': 500,
        'USE_REDIS_CACHE': 'default',
    },

}

