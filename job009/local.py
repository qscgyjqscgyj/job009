# Local settings template for job009 project.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'job009',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'qscgyjjygcsq',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

GEOIP_LOCATION_MODEL = 'user_profile.models.CustomLocation'

ACCOUNT_ACTIVATION_DAYS = 2

AUTH_USER_EMAIL_UNIQUE = True
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'aliestarten@gmail.com'
EMAIL_HOST_PASSWORD = 'qscgyjjygcsq'
EMAIL_PORT = 587


CAPTCHA_FOREGROUND_COLOR = '#000000'
CAPTCHA_LENGTH = 4
CAPTCHA_LETTER_ROTATION = (-10, 10)
CAPTCHA_FONT_SIZE = 60


THUMBNAIL_FORMAT = 'PNG'

import djcelery
djcelery.setup_loader()

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
BROKER_BACKEND = "djkombu.transport.DatabaseTransport"