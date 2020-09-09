import os
import environ
import datetime
import logging.config
import raven
from django.utils.translation import ugettext as _

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', '10.0.0.134')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET', "not-so-secret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == 'True'
STAGING = os.environ.get("STAGING") == 'True'
PROD = os.environ.get("PROD") == 'True'
LOCAL= os.environ.get("LOCAL", False) == 'True'
IS_DOCKER = os.environ.get("IS_DOCKER") is not None and os.environ.get("IS_DOCKER") == 'True'


ALLOWED_HOSTS = ['*']
CACHE_TIMEOUT = 300

db_password = os.environ.get("DB_PASSWORD", "")
db_user = os.environ.get("DB_USER", "")
db_name = os.environ.get("DB_NAME", "")
db_host = os.environ.get("DB_HOST", "")
db_port = os.environ.get("DB_PORT", "")

staging_db_password=os.environ.get("STAGING_DB_PASSWORD","")
staging_db_user=os.environ.get("STAGING_DB_USER","")
staging_db_name=os.environ.get("STAGING_DB_NAME","")
staging_db_host=os.environ.get("STAGING_DB_HOST","")
staging_db_port=os.environ.get("STAGING_DB_PORT","")

local_redis_location = os.environ.get("LOCAL_REDIS_HOST", "redis://redis:6379/0")
local_redis_session_location = os.environ.get("LOCAL_REDIS_SESSION_LOCATION", "redis://redis:6379/1")

staging_redis_location = os.environ.get("STAGING_REDIS_LOCATION", "0.0.0.0")
staging_redis_session_location = os.environ.get("STAGING_REDIS_SESSION_LOCATION", 6739)


aws_s3_access_id = os.environ.get('AWS_S3_ACCESS_KEY_ID', "")
aws_s3_access_key = os.environ.get('AWS_S3_SECRET_ACCESS_KEY', "")
jwt_key = os.environ.get('JWT_SECRET_KEY', "")
raven_dsn = os.environ.get('RAVEN_DSN', "")

if DEBUG or STAGING:
    print("===================================================")
    print("DEBUG = {0}".format(DEBUG))
    print("STAGING = {0}".format(STAGING))
    print("PROD = {0}".format(PROD))
    print("LOCAL = {0}".format(LOCAL))
    print("IS_DOCKER = {0}".format(IS_DOCKER))
    print("SECRET_KEY = {0}".format(SECRET_KEY))

    if DEBUG:
        print("DB_PASSWORD = {0}".format(db_password))
        print("DB_USER = {0}".format(db_user))
        print("DB_NAME = {0}".format(db_name))
        print("DB_HOST = {0}".format(db_host))
        print("DB_PORT = {0}".format(db_port))
    elif STAGING:
        print("DB_PASSWORD = {0}".format(staging_db_password))
        print("DB_USE = {0}".format(staging_db_user))
        print("DB_NAME = {0}".format(staging_db_name))
        print("DB_HOST = {0}".format(staging_db_host))
        print("DB_PORT = {0}".format(staging_db_port))

    if LOCAL:
        print("LOCAL_REDIS_HOST = {0}".format(local_redis_location))
        print("LOCAL_REDIS_SESSION_LOCATION = {0}".format(local_redis_session_location))
    if not LOCAL and STAGING:
        print("STAGING_REDIS_LOCATION = {0}".format(staging_redis_location))
        print("STAGING_REDIS_SESSION_LOCATION = {0}".format(staging_redis_session_location))

    print("JWT_SECRET_KEY = {0}".format(jwt_key))
    print("AWS_S3_ACCESS_KEY = {0}".format(aws_s3_access_key))
    print("AWS_S3_ACCESS_ID = {0}".format(aws_s3_access_id))
    print("RAVEN_DSN = {0}".format(raven_dsn))

# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd Party
    'raven.contrib.django.raven_compat',
    'rest_framework',
    'rest_framework_swagger',
    'dry_rest_permissions',
    'reversion',
    'storages',
    'cuser',
    'corsheaders',
    'debug_toolbar',


    # Quartet
    'quartet_epcis',
    'quartet_capture',
    'taskapp',

    # Project Specific
    'accounts',
    'contrib',
    'mdm',
    'chm',
    'api',
    'snm',
    'rules',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'cuser.middleware.CuserMiddleware',
    'reversion.middleware.RevisionMiddleware',

]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'api/templates'),
            os.path.join(BASE_DIR, 'accounts/templates'),
            os.path.join(BASE_DIR, 'api/templates/rest_framework_swagger'),

        ]
        ,
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

WSGI_APPLICATION = 'api.wsgi.application'
LOGIN_REDIRECT_URL = '/api/v1/'
LOGOUT_URL = '/'
LOGIN_URL = '/'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'api/media/')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'accounts.ForeSideUser'

# JWT
JWT_SECRET_KEY = jwt_key

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=7200),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1),

}

# REST Framework rest_framework.pagination.LimitOffsetPagination
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'api.views.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework_xml.parsers.XMLParser',
    ),
}

LOGGING_CONFIG = None
LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        # Log Handler for Sentry for `warning` and above
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },

    },
    'loggers': {
        # root logger
        '': {
            'level': 'WARNING',
            'handlers': ['console', 'sentry'],
        },
        'ragnor': {
            'level': LOGLEVEL,
            'handlers': ['console', 'sentry'],
            # required to avoid double logging with root logger
            'propagate': False,
        },
    },
})


# CORS
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
}

ASGI_APPLICATION = "api.routing.application"

