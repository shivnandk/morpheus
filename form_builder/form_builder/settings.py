from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-l24ni1o54b-w4ao*0f%sluf#)2$yltn=-%1(8-ocby9qih9wt@'

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',  # Add Jazzmin for a better admin interface
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'forms',  # Your app here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'form_builder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'form_builder.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

APPEND_SLASH = False

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'

# Path where static files will be collected (required for collectstatic command)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Additional directories for custom static files (like images)
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # This should already contain assets, including images
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin customization
JAZZMIN_SETTINGS = {
    "site_title": "My Admin",  # Title in the browser tab
    "site_header": "My Admin Panel",  # Title in the header
    "site_brand": "My App",  # Branding text in the header
    "welcome_sign": "Welcome to the My App Admin Panel",  # Welcome text for the admin page
    "topmenu_links": [
        {"name": "Home", "url": "/", "new_window": False},
        {"name": "Docs", "url": "https://docs.djangoproject.com/en/5.1/", "new_window": True},
    ],
    "user_avatar": "images/default-avatar.png",  # Set default avatar for users
    "theme": "modern",  # Modern theme for a fresh look
    "sidebar": "NAVBAR",  # Sidebar style (fixed or slideable)
    "show_ui_builder": True,  # Enable UI builder to customize admin interface visually
}
