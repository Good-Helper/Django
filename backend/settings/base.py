from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = None



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

    # 

    'django_vite',
] + RSV_APP



DJANGO_VITE = {
    'default': {
        'dev_mode': True,  # Режим разработки (True для разработки, False для production)
        'dev_server_port': 3000,  # Порт Vite Dev Server
        'manifest_path': BASE_DIR / 'frontend' / 'dist' / 'manifest.json',  # Путь к манифесту
        'static_url_prefix': 'assets/',  # Префикс для статики
        # 'server': {
        #     'https': False,  # Использовать HTTPS (True/False)
        # },
    }
}


# Import other settings modules
from .middleware import *
from .database import *
from .templates import *
from .internationalization import *
from .security import *
