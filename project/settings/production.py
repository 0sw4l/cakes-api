from .base import *

DEBUG = True

INSTALLED_APPS += ('gunicorn',)

ALLOWED_HOSTS = ['*']

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

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

WSGI_APPLICATION = 'project.wsgi.production.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6s6p0287p4fdj',
        'USER': 'zjjfbbesdkmtey',
        'PASSWORD': '0304e56e83e850ef0f7f2d4512853e4a26e305eb3d6320e1045daef5d6aa2700',
        'HOST': 'ec2-50-19-249-121.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
