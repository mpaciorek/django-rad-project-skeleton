# Local settings for {{ project_name }} project.
LOCAL_SETTINGS = True
from settings import *

DEBUG = True

#UNCOMMENT THIS LINE IN PRODUCTION MODE
# INSTALLED_APPS += ('gunicorn', )

#UNCOMMENT THIS LINE IN DEVELOPMENT MODE
# INSTALLED_APPS += ('gunicorn', )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}', # Or path to database file if using sqlite3.
        'USER': 'xxx',                             # Not used with sqlite3.
        'PASSWORD': 'xxx',                         # Not used with sqlite3.
        'HOST': 'localhost',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
