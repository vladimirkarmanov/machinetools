from .base import *

DEBUG = True
SECRET_KEY = '&%%-%z_s*$fj%(^(^0&%5%9!&5%5!0!65%*%VJ!^(^05-_3f&!$a$&u5&&&!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
