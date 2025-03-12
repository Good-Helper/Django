from pathlib import Path

# Определение базового пути
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Путь к директории с вашими шаблонами
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

# Настройки URL конфигурации
ROOT_URLCONF = 'app.urls'

# Настройки WSGI приложения
WSGI_APPLICATION = 'app.wsgi.application'


# Статические файлы (CSS, JavaScript, изображения)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Путь к вашей директории со статическими файлами
]


# Медиа файлы (загружаемые пользователями)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Путь к директории для медиа файлов
