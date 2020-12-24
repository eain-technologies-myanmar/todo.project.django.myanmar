_B='NAME'
_A=True
from pathlib import Path
import os.path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY='dhcn@&ux-62rm5gl_wts63oaknp)t=6gyd@yb+9tqeo2m233*('
DEBUG=_A
ALLOWED_HOSTS=[]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','TodoMyanmar']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF='todo.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[os.path.join(BASE_DIR,'templates')],'APP_DIRS':_A,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION='todo.wsgi.application'
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3',_B:BASE_DIR/'db.sqlite3'}}
AUTH_PASSWORD_VALIDATORS=[{_B:'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{_B:'django.contrib.auth.password_validation.MinimumLengthValidator'},{_B:'django.contrib.auth.password_validation.CommonPasswordValidator'},{_B:'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
USE_I18N=_A
USE_L10N=_A
USE_TZ=_A
STATIC_URL='/static/'