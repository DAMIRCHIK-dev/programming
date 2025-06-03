import os
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── Security & Debug ─────────────────────────────────────────────────────
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "CHANGE_ME_IN_PROD")
DEBUG = os.getenv("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# ─── Installed Apps ──────────────────────────────────────────────────────
INSTALLED_APPS = [
    # Jazzmin birinchi bo‘lsin, adminga tema berish uchun
    "jazzmin",

    # Django Contrib
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "rest_framework",
    "rest_framework.authtoken",
    "crispy_forms",
    "crispy_bootstrap5",
    "channels",

    # Local
    "inventory",
    "meals",
    "users",
    "reports",
    "websocket",

    # Celery Beat uchun
    "django_celery_beat",
]

# ─── Crispy Forms ────────────────────────────────────────────────────────
CRISPY_ALLOWED_TEMPLATE_PACKS = ("bootstrap5",)
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ─── Jazzmin settings ───────────────────────────────────────────────────
JAZZMIN_SETTINGS = {
    "site_title": "Kitchen Admin",
    "site_header": "Kitchen Dashboard",
    "site_brand": "Kindergarten Meals",
    "welcome_sign": "Welcome to the Admin Panel",
    "order_with_respect_to": ["auth", "inventory", "meals"],
    "icons": {
        "auth.user":               "fas fa-users",
        "inventory.ingredient":    "fas fa-pepper-hot",
        "inventory.ingredientdelivery": "fas fa-truck",
        "meals.meal":              "fas fa-utensils",
        "meals.servedmeal":        "fas fa-check-square",
    },
    "show_ui_builder": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "sidebar_nav_caption": True,
    "sidebar_style": "dark",
    "sidebar_nav_small_text": False,
    "theme": "flatly",       # BootsWatch nominatsiyalardan biri (masalan, flatly)
    "button_round": True,
    "input_round": True,
}

# ─── Middleware ─────────────────────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# ─── Templates ─────────────────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

# ─── WSGI & ASGI ────────────────────────────────────────────────────────
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# ─── Databases ───────────────────────────────────────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "bogcha_oshxona"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "admin1234"),
        # Docker’da “db” bo‘ladi, localda esa “localhost”
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

# ─── Password Validators ─────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ─── Internationalization ────────────────────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True

# ─── Static & Media ──────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ─── Authentication ─────────────────────────────────────────────────────
LOGIN_URL = "/api/users/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/api/users/login/"

# ─── REST Framework ─────────────────────────────────────────────────────
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
}

# ─── Channels (WebSocket) ───────────────────────────────────────────────
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            # Docker konteyner ichida Redis “redis” nomidan topiladi:
            "hosts": [os.getenv("REDIS_URL", "redis://redis:6379/0")]
        },
    }
}

# ─── Celery ──────────────────────────────────────────────────────────────
CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE

# ─── Email Backend ──────────────────────────────────────────────────────
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ─── Defaults ───────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Agar sizning loyiha ichida alohida “static/” va “templates/static” papkalar bo‘lsa:
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "templates" / "static",
]
