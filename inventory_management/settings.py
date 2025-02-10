import os
from pathlib import Path

# ========================
# ✅ Base Project Settings
# ========================

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security key (Use a secret key for production, DO NOT expose this publicly)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')

# Debug mode (Set to False in production)
DEBUG = True  # Change to False in production for security

# Allowed hosts (Ensure only trusted domains are added in production)
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
    'rest_framework',          # Django REST framework (for API support)
    'corsheaders',             # Cross-Origin Resource Sharing (CORS) handling
    'inventory',               # Custom inventory management app
]


# ===========================
# ✅ Middleware Configuration
# ===========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Enable CORS middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protects against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevents Clickjacking attacks
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
            BASE_DIR / "inventory/templates",  # Ensure Django looks for templates in the inventory app
            BASE_DIR / "templates",  # Fallback for project-level templates
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
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation (For enforcing strong passwords)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ===========================
# ✅ Localization Settings
# ===========================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ===========================
# ✅ Static and Media Files
# ===========================

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Serve media files in development
if DEBUG:
    from django.conf.urls.static import static


# ===========================
# ✅ CORS Configuration (For API security)
# ===========================

CORS_ALLOW_ALL_ORIGINS = False  # Disable in production (Only allow trusted origins)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
]  # Add your frontend domain here
CORS_ALLOW_CREDENTIALS = True


# ===========================
# ✅ Secure Cookies Setup 
# ===========================

# Session Cookies Security
SESSION_COOKIE_SECURE = not DEBUG  # Secure cookies in production
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access
SESSION_COOKIE_SAMESITE = 'Strict'  # Prevent cross-site request attacks

# CSRF Cookies Security
CSRF_COOKIE_SECURE = not DEBUG  # Secure in production
CSRF_COOKIE_HTTPONLY = True  # Prevent JavaScript access
CSRF_COOKIE_SAMESITE = 'Strict'  # Stronger protection against CSRF

# Security Redirects (Forces HTTPS in production)
SECURE_SSL_REDIRECT = not DEBUG  # Redirect HTTP to HTTPS

# HSTS (HTTP Strict Transport Security) - Forces HTTPS (Only in Production)
SECURE_HSTS_SECONDS = 31536000  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True  # Enables HSTS Preloading


# ===========================
# ✅ Security Hardening
# ===========================

# Prevent Clickjacking Attacks
X_FRAME_OPTIONS = 'DENY'

# Enable Browser XSS Protection
SECURE_BROWSER_XSS_FILTER = True

# Prevent MIME type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# HTTP Strict Transport Security (HSTS) - Enforces HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 Year (Only Enable in Production)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True  # Enable HSTS Preloading

# Default auto primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
