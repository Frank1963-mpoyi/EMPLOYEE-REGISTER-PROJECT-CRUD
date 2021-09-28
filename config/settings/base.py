import      os
from        decouple                        import      config
import      configparser


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = [ 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # App Project
    'register.apps.web.blog',
    
    # 3rd party
    'crispy_forms',
    'django.contrib.sites',  # remember to put site_id

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

LOGIN_REDIRECT_URL ='/'

ACCOUNT_LOGOUT_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

CONFIG_DIR = os.path.join(BASE_DIR, 'config/')

parser = configparser.ConfigParser()
parser.read_file(open(os.path.join(CONFIG_DIR, 'app.ini')))

#Done with postgresql 
DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql_psycopg2',
        'NAME'      : parser.get('crud', 'name'),
        'USER'      : parser.get('crud', 'user'),
        'PASSWORD'  : parser.get('crud', 'password'),
        'HOST'      : parser.get('crud', 'host') or '127.0.0.1',
        'PORT'      : parser.getint('crud', 'port') or '5432',

    }
}

# Auth
AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

]

ACCOUNT_EMAIL_REQUIRED              = True
ACCOUNT_USERNAME_REQUIRED           = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER            = True
ACCOUNT_AUTHENTICATION_METHOD       = 'email' # login with email
ACCOUNT_UNIQUE_EMAIL                = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'register/templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE       = 'Africa/Johannesburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
BASE_PATH                   = os.path.join(BASE_DIR)
APP_STATIC                  = '/static/'

STATICFILES_DIRS            =[ os.path.join(BASE_DIR, 'register/static')]

STATIC_URL                  = '/static/'
STATIC_ROOT                 = os.path.join(BASE_PATH,  'register/static/staticfiles')

MEDIA_URL                   = '/media/'
MEDIA_ROOT                  = os.path.join(BASE_DIR,  f'{APP_STATIC }/media')

SITE_ID = 1

#DEFAULT_AUTO_FIELD = 'django.models.models.BigAutoField'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'