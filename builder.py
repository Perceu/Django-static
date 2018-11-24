import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
ALLOWED_HOST = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG = DEBUG,
    SECRET_KEY = 'THISASECRETKEY',
    ROOT_URLCONF = 'sitebuilder.urls',
    ALLOWED_HOST = ALLOWED_HOST,
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XframeOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {},
        },
    ],
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR,'pages'),
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR,'_build'),
    STATIC_ROOT=os.path.join(BASE_DIR,'_build', 'static'),
    STATIC_URL='/static/'
)

application = get_wsgi_application()

if __name__=="__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)