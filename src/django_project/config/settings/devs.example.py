from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ['*']
    INTERNAL_IPS = ("127.0.0.1", "localhost")
else:
    ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
# ex: b26)zfeac&3d%_s5ao6$u4!!e_6rruw6@$5r%ek$#spm3h%#pq
# Please, change default secret key.
# Command: ./manage.py seckeygen --settings=config.settings.devs
SECRET_KEY = 'b26)zfeac&3d%_s5ao6$u4!!e_6rruw6@$5r%ek$#spm3h%#pq'

# Database (for dev only)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ASSETS_MEDIA_DIR, 'db.sqlite3'),
    }
}