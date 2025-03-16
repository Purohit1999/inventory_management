import os
from pathlib import Path

# ========================
# ✅ Base Project Settings
# ========================

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔒 Security key (Use an environment variable in production)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')

# 🔧 Debug mode (Set to False in production)
DEBUG = True  # Change to False in production

# 🌐 Allowed hosts (Set correctly in production)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


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
    
    # ✅ Custom apps
    'inventory',         # Inventory management app
]


# ===========================
# ✅ Middleware Configuration
# ===========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
# ✅ Database Configuration (Default: SQLite)
# ===========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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
STATIC_ROOT = BASE_DIR / 'staticfiles'  # ✅ Necessary for `collectstatic`

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # ✅ Ensures media uploads are stored correctly


# ===========================
# ✅ Security Hardening
# ===========================

SECURE_SSL_REDIRECT = not DEBUG  # Redirect HTTP to HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
