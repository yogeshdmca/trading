import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'q9+1cli039zfw564d*=aw=8+&dfvux8(+=+45v$z&tn85&v7b@'

DEBUG =False

ADMINS = (
     ('Yogesh', 'alen@geitpl.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'widget_tweaks',
    'accounts',
    'trade',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trading.urls'

# Add templates to DIRS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  #modify this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ws4redis.context_processors.default',
            ],
        },
    },
]

WSGI_APPLICATION = 'trading.wsgi.application'





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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1



STATIC_URL = '/static/'



STATICFILES_DIRS = [
os.path.join(BASE_DIR, "static"),
]



AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_SUBJECT_PREFIX='Iqptionexperts'

ACCOUNT_LOGIN_REDIRECT_URL='/dashbord/'

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 30

ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SESSION_REMEMBER =False


ACCOUNT_EMAIL_VERIFICATION = None

ACCOUNT_USERNAME_REQUIRED = False


AUTH_PROFILE_MODULE = 'account.Profile'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'geitpl@gmail.com'
EMAIL_HOST_PASSWORD = 'purnima2014'
DEFAULT_FROM_EMAIL = 'no-reply@iqoptionexperts.com'


STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")

DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': 'trading',
             'USER': 'trading',
             'PASSWORD': 'geitpl@#$123',
             'HOST': 'localhost',
             'PORT': '5432',
         }
}




INSTALLED_APPS += [
    'ws4redis'
]

WEBSOCKET_URL = '/ws/'
WS4REDIS_PREFIX = 'ws'

WSGI_APPLICATION = 'ws4redis.django_runserver.application'
WS4REDIS_EXPIRE = 1

APP_ID = 2557


EMAIL_HOST = 'smtp.pepipost.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'alengeitpl'
EMAIL_HOST_PASSWORD = 'OMsai@ram1'
DEFAULT_FROM_EMAIL = 'info@iqoptionexperts.com'



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}