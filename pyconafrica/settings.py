"""
Django settings for pyconafrica project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from datetime import datetime
from pathlib import Path

try:
    from .secrets import *
except ImportError:
    raise Exception(
        "A secrets.py file is required to run this project, if not provided contact Mannie Young - https://twitter.com/mawy_7"
    )


ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split()
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


ALLOWED_HOSTS = ["*"]

LOGIN_REDIRECT_URL = "/accounts/profile/"
SIGNUP_REDIRECT_URL = "/accounts/profile/"
LOGOUT_REDIRECT_URL = "/"

# Application definition

INSTALLED_APPS = [
    "grappelli",
    "cloudinary",
    "cloudinary_storage",
    "gamma_cloudinary",
    "django.contrib.admin",
    'django.contrib.sites',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "avatar",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_recaptcha",
    "django_slugify_processor",
    "django_countries",
    "django_summernote",
    "django_extensions",
    "django_robohash",
    "embed_video",
    "imagekit",
    "import_export",
    "rest_framework",
    "tinymce",
    "sorl.thumbnail",
    #'newsletter',
    "markdownx",
    #'mdeditor',
    #'markitup',
    "hitcount",
    # APPS
    "about",
    "contact",
    "registration",
    "coc",
    "event",
    "faq",
    "fin_aid",
    "health_safety_guideline",
    "home",
    "privacypolicy",
    "pycon2020",
    "pyconafrica2019",
   #"schedule",
    'conference_schedule',
    "speakers",
    "sponsors",
    "sponsor_us",
    "talks",
    "tickets",
    'cms',
]

MIDDLEWARE = [ 
    #"django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]



ROOT_URLCONF = "pyconafrica.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.media",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "pyconafrica.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Accra"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Full filesystem path to the project.
PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)
 

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# if DEBUG:
#     STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    				 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', 
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
   

#STATICFILES_STORAGE = 'gamma_cloudinary.storage.StaticCloudinaryStorage'
DEFAULT_FILE_STORAGE = 'gamma_cloudinary.storage.CloudinaryStorage' 
  

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

 


# Sets the default template pack for the project
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


# Registration App account settings
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = "[PyCon Africa]"
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False


X_FRAME_OPTIONS = "SAMEORIGIN"

SUMMERNOTE_THEME = "bs4"  # Show summernote with Bootstrap4
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    "iframe": True,
    # You can put custom Summernote settings
    "summernote": {
        # As an example, using Summernote Air-mode
        "airMode": False,
        # Change editor size
        "width": "100%",
        "height": "480",
        # Use proper language setting automatically (default)
        "lang": None,
    },
    # Need authentication while uploading attachments.
    "attachment_require_authentication": True,
    # You can disable attachment feature.
    "disable_attachment": False,
    # Lazy initialize
    # If you want to initialize summernote at the bottom of page, set this as True
    # and call `initSummernote()` on your page.
    "lazy": True,
}

TINYMCE_DEFAULT_CONFIG = {
    "content_css": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css",
    "selector": "textarea",
    "theme": "modern",
    "plugins": "link image preview codesample contextmenu table code lists",
    "toolbar1": "formatselect | bold italic underline | alignleft aligncenter alignright alignjustify "
    "| bullist numlist | outdent indent | table | link image | forecolor |backcolor | codesample | preview code",
    "contextmenu": "formats | link image",
    "menubar": True,
    "inline": False,
    "statusbar": True,
    "width": "auto",
    "height": 360,
}
TINYMCE_COMPRESSOR = True
TINYMCE_EXTRA_MEDIA = {
    "css": {
        "all": [...],
    },
    "js": [...],
}


# Using the new No Captcha reCaptcha
NOCAPTCHA = True

# Sets the default site
SITE_ID = 1

AVATAR_MAX_AVATARS_PER_USER = 1

AVATAR_ALLOWED_FILE_EXTS = (".jpg", ".jpeg", ".png")

HASHIDS_SALT = ("some_random_string",)


MARKDOWNX_MARKDOWNIFY_FUNCTION = "markdownx.utils.markdownify"

## markdownify
MARKDOWNIFY_WHITELIST_TAGS = [
    "a",
    "abbr",
    "acronym",
    "b",
    "blockquote",
    "em",
    "i",
    "li",
    "ol",
    "p",
    "strong",
    "ul",
    "pre",
    "code",
]
MARKDOWNIFY_WHITELIST_PROTOCOLS = [
    "http",
    "https",
]
MARKDOWNX_MEDIA_PATH = datetime.now().strftime("markdownx/%Y/%m/%d")
MARKDOWNIFY_LINKIFY_PARSE_EMAIL = True
MARKDOWNX_EDITOR_RESIZABLE = True
MARKDOWNX_MEDIA_PATH = "markdownx/"
MARKDOWNIFY_LINKIFY_SKIP_TAGS = [
    "pre",
    "code",
]
MARKDOWNIFY_WHITELIST_ATTRS = [
    "href",
    "src",
    "alt",
    "class",
]
