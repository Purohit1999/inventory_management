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
DEBUG = os.getenv('DEBUG', 'False') == 'True'  # ✅ Reads from env variable

# 🌐 Allowed hosts (Updated for Heroku deployment)
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME', 'inventory-mgmt-system')  # ✅ Default to your app name

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    f'{HEROKU_APP_NAME}.herokuapp.com',  # ✅ Ensure Heroku app domain is included
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
    'rest_framework',    # Django REST Framework (for API support)
    'corsheaders',       # CORS handling for APIs
    'whitenoise.runserver_nostatic',  # ✅ Handles static files for Heroku

    # ✅ Custom apps
    'inventory',         # Inventory management app
]

# ===========================
# ✅ Middleware Configuration
# ===========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Handles static files on Heroku
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
            BASE_DIR / "inventory/templates",  # ✅ Ensures templates are found
            BASE_DIR / "templates",  # ✅ Global templates directory (Optional)
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
# ✅ Database Configuration (Handles Local & Heroku DB)
# ===========================

DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',  # ✅ Default to SQLite for local use
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
LOGIN_URL = '/accounts/login/'  # ✅ Fixes login redirection issue
LOGIN_REDIRECT_URL = '/'  # ✅ Redirects users after login
LOGOUT_REDIRECT_URL = '/accounts/login/'  # ✅ Redirect after logout

# ===========================
# ✅ Static and Media Files
# ===========================

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # ✅ Ensures correct static files location
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # ✅ Required for Heroku deployment

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # ✅ Ensures media uploads are stored correctly

# ✅ Serve static files with WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ===========================
# ✅ Security Hardening
# ===========================

SECURE_SSL_REDIRECT = not DEBUG  # Redirect HTTP to HTTPS in production
SECURE_HSTS_SECONDS = 31536000  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# ===========================
# ✅ Default Auto Field
# ===========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
