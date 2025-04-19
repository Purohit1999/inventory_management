from pathlib import Path
from decouple import config
import dj_database_url
import os

# ===========================
# ✅ BASE CONFIGURATION
# ===========================

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY", default="please-change-this-in-prod")
DEBUG = config("DEBUG", default=False, cast=bool)

HEROKU_APP_NAME = config("HEROKU_APP_NAME", default="inventory-mgmt-system")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    f"{HEROKU_APP_NAME}.herokuapp.com",
    ".herokuapp.com",
]

CSRF_TRUSTED_ORIGINS = [
    f"https://{HEROKU_APP_NAME}.herokuapp.com",
    "https://*.herokuapp.com",
]

# ===========================
# ✅ INSTALLED APPS
# ===========================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "corsheaders",
    "whitenoise.runserver_nostatic",
    "widget_tweaks",

    # Local apps
    "inventory",
]

# ===========================
# ✅ MIDDLEWARE
# ===========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ===========================
# ✅ URL Configuration
# ===========================

ROOT_URLCONF = "inventory_management.urls"
WSGI_APPLICATION = "inventory_management.wsgi.application"

# ===========================
# ✅ TEMPLATES
# ===========================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "inventory" / "templates",
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
# ✅ DATABASE CONFIGURATION
# ===========================

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"),
        conn_max_age=600
    )
}

# ===========================
# ✅ AUTHENTICATION SETTINGS
# ===========================

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/products"
LOGOUT_REDIRECT_URL = "/"

# ===========================
# ✅ STATIC & MEDIA FILES
# ===========================

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"] if (BASE_DIR / "static").exists() else []
STATIC_ROOT = BASE_DIR / "staticfiles"

# For Heroku: Enable whitenoise in both local & production
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
    if "DYNO" in os.environ
    else "django.contrib.staticfiles.storage.StaticFilesStorage"
)

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ===========================
# ✅ SECURITY SETTINGS
# ===========================

SECURE_SSL_REDIRECT = not DEBUG and "DYNO" in os.environ
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "SAMEORIGIN"  # SAFER option than "ALLOWALL"

# ===========================
# ✅ CORS SETTINGS
# ===========================

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# ===========================
# ✅ LOGGING
# ===========================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG" if DEBUG else "INFO",
    },
}

# ===========================
# ✅ AUTO FIELD
# ===========================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
