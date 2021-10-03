"""
Django settings for analytics project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Secret key is stored as an environmental variable on the server to avoid anyone peeking in the source file.
SECRET_KEY = os.environ["SECRET_KEY"]

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
    'dashboard'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.TimezoneMiddleware'
]

ROOT_URLCONF = 'analytics.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'analytics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
Sets X-XSS-Protection: 1; mode=block header on all responses that do not already have it
Modern browsers typically ignore this header, but it's a good idea for supporting older browsers
"""
# SECURE_BROWSER_XSS_FILTER = True

"""
If there is any functionality baked into the site that allows users to upload content files to our server, then sometimes
the browser can override the Content-Type header on the content getting fetched, if the browser thinks that the server is not 
configured correctly. However, a malicious actor can use this functionality to spoof the server into accepting content
that would otherwise be rejected as unsafe.
"""
# SECURE_CONTENT_TYPE_NOSNIFF

"""
Modern browsers can be told to refuse to connect to the site for a while if the connection is being made by HTTP instead
of the preferred HTTPS, where the length of the wait can be set here. This can be a valuable tool if one is concerned 
that incoming traffic to the webpage may have been compromised by an HTTP S-stripping attack. Frequently, this would be
orchestrated by a man in the middle attack.

CHANGING THESE IF YOU'RE NOT SURE ABOUT THEM WILL DISABLE YOUR SITE.
"""
# SECURE_HSTS_INCLUDE_SUBDOMAINS
# SECURE_HSTS_PRELOAD
# SECURE_HSTS_SECONDS

"""
Sometimes when networks are programmed, the proxy gateway by which traffic enters the network will sometimes dump 
unencrypted traffic into the lower levels of the network. -IF- there is a proxy server that is doing this for a good,
non-lazy reason, then Django will only see unencrypted HTTP traffic coming and and may unnecessarily restrict that 
traffic as unsecure.

The example below would tell Django that anything reaching it by HTTP that is stamped with a X-Forwarded-Proto header
can be considered as HTTPS traffic since it securely entered an ingress point and was already processed. 

ONLY SET THIS VALUE IF YOU ARE USING A PROXY SERVER.
ONLY SET THIS VALUE IF YOUR PROXY STRIPS THE X-Forwarded-Proto HEADER FROM ALL INCOMING TRAFFIC.
ONLY SET THIS VALUE IF THE PROXY THEN RESETS THE X-Forwarded-Proto HEADER BACK ONTO ITS OUTGOING TRAFFIC.

MESSING THIS VALUE UP WILL CAUSE OUR SITE TO GET UBER PWNED.
"""
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "HTTPS")

"""
Secure Redirect Except allows us to supply one or more regexes to scour our pages for exemptions to the HTTP/HTTPS 
forwarding policy.

Secure SSL Host redirects all traffic to that host regardless of how it got here. If we use this
option we can also supply a regex to SECURE_SSL_REDIRECT to exempt certain pages from being forwarded.

Secure SSL Redirect causes the security middleware to enforce a policy regarding whether HTTP, HTTPS or both HTTP and HTTPS
connections are accepted. A value of true enforces a permanent HTTP 301 redirect that forwards all connections to HTTPS.

Note: this option (from a security standpoint) is best set to true, but from a standpoint of performance, if this could be done
in a reverse proxy server (NGINX) or a front-end load balancer, it is more appropriate to set this to false and let the front-end
server handle the lifting. This flag is primarily meant for situations where that type of architecture isn't possible. 
"""
# SECURE_SSL_REDIRECT = True
# SECURE_SSL_HOST = "URI_OF_REDIRECTION"
# SECURE_REDIRECT_EXEMPT = []


"""
Tells the browser to send the full URL for the referrer when the link is same-origin with no https downgrading; otherwise
do not send anything
"""
SECURE_REFERRER_POLICY = "same-origin"
