import os
from pathlib import Path
import dj_database_url

# ===========================
# ✅ BASE CONFIGURATION
# ===========================

BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Security Key (Keep Secret in Production)
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "3fM2QpX1L0iW5m7dO9kG-JR8yF6cT4aY2pNbVZqHdXs=")

# ✅ Debug Mode (Only Enable for Local Development)
DEBUG = os.getenv("DEBUG", "False") == "True"

# ✅ Allowed Hosts (Update for Deployment)
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "inventory-mgmt-system")
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    f"{HEROKU_APP_NAME}.herokuapp.com",
    ".herokuapp.com",
]

# ✅ CSRF Trusted Origins (Avoid Cross-Site Request Forgery Issues)
CSRF_TRUSTED_ORIGINS = [
    f"https://{HEROKU_APP_NAME}.herokuapp.com",
    "https://*.herokuapp.com",
]

# ===========================
# ✅ INSTALLED APPLICATIONS
# ===========================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",  # ✅ API Support
    "corsheaders",  # ✅ CORS Support for External API Calls
    "whitenoise.runserver_nostatic",  # ✅ Static Files Compression
    "inventory",  # ✅ Your Inventory App
]

# ===========================
# ✅ MIDDLEWARE CONFIGURATION
# ===========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ✅ Faster Static Files Serving
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # ✅ Enable Cross-Origin Requests
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ===========================
# ✅ URL CONFIGURATION
# ===========================

ROOT_URLCONF = "inventory_management.urls"
WSGI_APPLICATION = "inventory_management.wsgi.application"

# ===========================
# ✅ TEMPLATES CONFIGURATION
# ===========================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "inventory/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ===========================
# ✅ DATABASE CONFIGURATION (PostgreSQL for Heroku)
# ===========================

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}

# ===========================
# ✅ AUTHENTICATION SETTINGS
# ===========================

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

# ===========================
# ✅ STATIC & MEDIA FILES CONFIGURATION
# ===========================

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"] if (BASE_DIR / "static").exists() else []
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ===========================
# ✅ SECURITY SETTINGS (For Deployment)
# ===========================

SECURE_SSL_REDIRECT = not DEBUG and "HEROKU" in os.environ
SECURE_HSTS_SECONDS = 31536000  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = "DENY"
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


# ===========================
# ✅ CORS CONFIGURATION (For APIs)
# ===========================

CORS_ALLOWED_ORIGINS = [
    f"https://{HEROKU_APP_NAME}.herokuapp.com",
    "http://localhost:8000",
]

# ===========================
# ✅ LOGGING CONFIGURATION (For Debugging & Production)
# ===========================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG" if DEBUG else "INFO",
    },
}

# ===========================
# ✅ DEFAULT SETTINGS
# ===========================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
