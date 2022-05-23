# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y0p+2fo*6+0p@)=k37h77oa8$xlxzo=fc==%pqftzx^4r45iot'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '555429ea',
    }
}
