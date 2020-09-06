from my_personal_website.common import *
import os
import django_heroku

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False



SECRET_KEY = os.environ['SECRET_KEY']

#update this to be heroku
ALLOWED_HOSTS = ['0.0.0.0', '.herokuapp.com']

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'website/static'),
# )

django_heroku.settings(locals())