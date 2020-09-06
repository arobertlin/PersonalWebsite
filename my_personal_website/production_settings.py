from my_personal_website.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

#update this to be heroku
ALLOWED_HOSTS = ['0.0.0.0', '.herokuapp.com']