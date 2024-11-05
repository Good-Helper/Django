# app/settings/base.py

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0$0ke8d+*e)#aj7l!$44b0w4a&wc5(mfw6@=lf1(u=2jdg%ljv'



# Application definition
RSV_APP = [

]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + RSV_APP



# Import other settings modules
from .middleware import *
from .database import *
from .templates import *
from .internationalization import *
from .security import *
