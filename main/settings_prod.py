from .settings import *

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'multipage',
       'USER': 'multipageuser',
       'PASSWORD': '123multipage',
       'HOST': 'localhost',
       'PORT': '',
   }
}
DEBUG = False
