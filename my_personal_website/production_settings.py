from my_personal_website.common import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

#update this to be heroku
ALLOWED_HOSTS = ['0.0.0.0', '.herokuapp.com']

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')