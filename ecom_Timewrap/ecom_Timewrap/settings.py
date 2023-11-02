"""
Django settings for ecom_Timewrap project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product',
    'user',
    'home',
    'admin_home',
    'categories',
    'admin_product',
    'order',
    'cloudinary',


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

ROOT_URLCONF = 'ecom_Timewrap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.views.category',
                'product.views.brand',
                'product.views.material',
                'product.views.color',
                'admin_home.context_processor.revenue',
                'admin_home.context_processor.counter',
                
            ],
        },
    },
]
    
WSGI_APPLICATION = 'ecom_Timewrap.wsgi.application'
AUTH_USER_MODEL='user.Account'
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
  'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME':os.getenv('Database'),
       'USER':os.getenv('User_name'),
       'PASSWORD':os.getenv('Password'),
       'HOST':os.getenv('Hostname'),
       'PORT':os.getenv('Port')
   }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

MEDIA_URL='/MEDIA/'

MEDIA_ROOT=BASE_DIR/ 'uploads'

from django.contrib.messages import constants as messages
MESSAGE_TAGS={
    messages.ERROR:'danger'
    
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = 'login'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER =config('mail')
EMAIL_HOST_PASSWORD =config('mail_pwd')
EMAIL_USE_TLS = True




KEY=os.getenv('id')
SECRET=os.getenv('secret')



CLOUDINARY_STORAGE = {
'CLOUD_NAME':config('Cloud_Name'),
'API_KEY': config('API_KEY'),
'API_SECRET': config('Secret_Key'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'