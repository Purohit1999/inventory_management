import os
from pathlib import Path
import dj_database_url  # ✅ Required for Heroku database support

# ========================
# ✅ Base Project Settings
# ========================

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔒 Security key (Now set via environment variable)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

# 🔧 Debug mode (Set to False in production)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# 🌐 Allowed hosts (Updated for Heroku deployment)
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME', 'inventory-mgmt-system-8e7f20e57e43')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    f'{HEROKU_APP_NAME}.herokuapp.com',  # ✅ Ensures Heroku app domain is included
]

# ===========================
# ✅ Installed Applications
# ===========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ Third-party apps
    'rest_framework',    
    'corsheaders',       
    'whitenoise.runserver_nostatic',  

    # ✅ Custom apps
    'inventory',         
]

# ===========================
# ✅ Middleware Configuration
# ===========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===========================
# ✅ URL and WSGI Configuration
# ===========================

ROOT_URLCONF = 'inventory_management.urls'
WSGI_APPLICATION = 'inventory_management.wsgi.application'

# ===========================
# ✅ Templates Configuration
# ===========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "inventory/templates",  
            BASE_DIR / "templates",  
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

# ===========================
# ✅ Database Configuration
# ===========================

DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',  
        conn_max_age=600,  
    )
}

# ===========================
# ✅ Authentication Settings
# ===========================

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  
]

# 🔐 Authentication Redirects
LOGIN_URL = '/accounts/login/'  
LOGIN_REDIRECT_URL = '/'  
LOGOUT_REDIRECT_URL = '/accounts/login/'  

# ===========================
# ✅ Static and Media Files
# ===========================

STATIC_URL = '/static/'

# ✅ Ensure static files exist before deployment
STATICFILES_DIRS = [
    BASE_DIR / 'static',
] if (BASE_DIR / 'static').exists() else []

STATIC_ROOT = BASE_DIR / 'staticfiles'  

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  

# ✅ Serve static files with WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ===========================
# ✅ Security Hardening
# ===========================

SECURE_SSL_REDIRECT = not DEBUG  
SECURE_HSTS_SECONDS = 31536000  
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# ===========================
# ✅ Logging Configuration (For Heroku)
# ===========================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'INFO',
    },
}

# ===========================
# ✅ Default Auto Field
# ===========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
