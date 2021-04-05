from .base import *
import dj_database_url

SECRET_KEY = os.getenv('SECRET_KEY', 'test_secret_key')

LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
   'handlers': {
       'console': {
           'class': 'logging.StreamHandler',
           'level': 'DEBUG',
           'formatter': 'verbose',
       },
   },
   'loggers': {
       '': {
           'handlers': ['console'],
           'level': 'DEBUG',
           'formatter': 'verbose',
           'propagate': True,
       },
       'django.db': {
           'level': 'INFO',
           'formatter': 'verbose',
       },
       'django.request': {
           'handlers': ['console', ],
           'level': 'INFO',
           'propagate': True,

       },
   },
}
