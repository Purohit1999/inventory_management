import os
from pathlib import Path
import dj_database_url

# ========================
# ✅ Base Project Settings
# ========================

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔒 Security Key (Set via Heroku Environment Variable)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '3fM2QpX1L0iW5m7dO9kG-JR8yF6cT4aY2pNbVZqHdXs=')

# 🔧 Debug Mode (Set via Heroku)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# 🌐 Allowed Hosts (Fixing Bad Request 400 Error)
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME', 'inventory-mgmt-system')
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    f'{HEROKU_APP_NAME}.herokuapp.com',
]

# ✅ CSRF Trusted Origins (Fixing CSRF Issues)
CSRF_TRUSTED_ORIGINS = [
    f"https://{HEROKU_APP_NAME}.herokuapp.com"
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
    'whitenoise.runserver_nostatic',  # ✅ WhiteNoise for static files

    # ✅ Custom apps
    'inventory',
]

# ===========================
# ✅ Middleware Configuration
# ===========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Serve static files efficiently
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # ✅ Enable CORS
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
            BASE_DIR / "templates",  # ✅ Global templates directory
            BASE_DIR / "inventory/templates",  # ✅ App-specific templates
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
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',  # ✅ Default SQLite for local development
        conn_max_age=600,  # ✅ Optimize for Heroku
    )
}

# ===========================
# ✅ Authentication Settings
# ===========================

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # ✅ Default authentication system
]

# 🔐 Authentication Redirects
LOGIN_URL = '/accounts/login/'  
LOGIN_REDIRECT_URL = '/'  
LOGOUT_REDIRECT_URL = '/accounts/login/'  

# ===========================
# ✅ Static and Media Files
# ===========================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ Serve static files with WhiteNoise (Best practice for Heroku)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ===========================
# ✅ Security Hardening
# ===========================

SECURE_SSL_REDIRECT = not DEBUG
SECURE_HSTS_SECONDS = 31536000  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# ===========================
# ✅ Logging Configuration (For Debugging on Heroku)
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
