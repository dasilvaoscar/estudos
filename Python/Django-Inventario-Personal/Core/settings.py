import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

SECRET_KEY = '=+eq6ue8oz^evix75tcnzpkr_k)9!!rdehf7ltiarg5d+i0^jj'

DEBUG = True

'''
AUTHENTICATION_BACKENDS = (
    "django_python3_ldap.auth.LDAPBackend",
)

LDAP_AUTH_SEARCH_BASE = 'OU=TESTE-TESTE,DC=TESTE,DC=TESTE'

LDAP_AUTH_CONNECTION_USERNAME = 'intranet'
LDAP_AUTH_CONNECTION_PASSWORD = '5xI481G!nhifMAqCuoUo'

LDAP_AUTH_USER_FIELDS = {
  "username": "sAMAccountName",
  "first_name": "givenName",
  "last_name": "sn",
  "email": "mail",
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"
LDAP_AUTH_SYNC_USER_RELATIONS = "django_python3_ldap.utils.sync_user_relations"
LDAP_AUTH_FORMAT_SEARCH_FILTERS = "app_custom.views.custom_format_search_filters"
LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory"
LDAP_AUTH_URL = 'ldap://10.1.5.220:389'
LDAP_USER_SEARCH_FILTER = "(&(sAMAccountName=%s)(objectClass=user))"
LDAP_AUTH_OBJECT_CLASS = 'organizationalPerson'  #User or organizationalPerson
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = 'TESTE'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django_python3_ldap": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
'''




ALLOWED_HOSTS = ['*']

IMPORT_EXPORT_USE_TRANSACTIONS = True

INSTALLED_APPS = [

    ### Import Apps
    'jet.dashboard',
    'jet',
    'django_python3_ldap',
    'adminactions',
    'global_permissions',

    ### Apps Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    ### All Apps
    'app_home_page.apps.AppHomePageConfig',
    'app_cardapio.apps.AppCardapioConfig',
    'app_valores.apps.AppValoresConfig',
    'app_estoque.apps.AppEstoqueConfig',
    'app_custom.apps.AppCustomConfig',
    'app_licencas.apps.AppLicencasConfig',
    'app_ramais.apps.RamaisConfig',
    'app_inventario.apps.InventarioConfig',
    
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'login_required.middleware.LoginRequiredMiddleware',
    'Core.middleware.LoginRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite',
    }
}

PASSWORD_RESET_TIMEOUT_DAYS = 120

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000000

## Jet

JET_DEFAULT_THEME = 'light-blue'

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

LOGIN_REQUIRED_IGNORE_PATHS = [
    r'/admin/$',
    r'/admin/login/$',
]

LOGOUT_REDIRECT_URL = '/admin/login'
LOGIN_URL = 'admin/login'
LOGIN_REDIRECT_URL = '/ramais/'

