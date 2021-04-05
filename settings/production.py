from .base import *


CONFIGURED_ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
for host in CONFIGURED_ALLOWED_HOSTS:
    if host:
        ALLOWED_HOSTS.append(host)

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}

DATABASES['default']['CONN_MAX_AGE'] = 7200

DATABASES['default']['OPTIONS'] = {
    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    'use_unicode': True,
}
