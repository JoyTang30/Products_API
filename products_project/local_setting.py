# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ibf1$a%vav03z!_6z957hnb$inw+cf9d25j4=55aai&-r0@zt('


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_project',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}