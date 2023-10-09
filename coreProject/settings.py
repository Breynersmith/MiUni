import environ
import os


from pathlib import Path

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env('DEBUG')



# Define la ruta base del proyecto como la ruta del archivo actual (settings.py) resuelta hacia arriba dos veces
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env('SECRET_KEY')

# ADVERTENCIA DE SEGURIDAD: No ejecutes con el modo de depuración activado en producción


# Lista de hosts permitidos para esta aplicación (en blanco para permitir todos los hosts en desarrollo)
ALLOWED_HOSTS = []

# Definición de las aplicaciones instaladas en el proyecto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'academica',
    'tailwind',
    'theme',
    
]

# Middleware de Django utilizado para procesar solicitudes y respuestas
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de la URL raíz del proyecto
ROOT_URLCONF = 'coreProject.urls'

# Configuración de plantillas HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'academica\plantillas',  # Directorio donde se encuentran las plantillas HTML personalizadas
        ],
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

# Configuración de la aplicación WSGI para servir la aplicación web
WSGI_APPLICATION = 'coreProject.wsgi.application'

# Configuración de la base de datos (utilizando SQLite en este caso)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'miuniversidad.sqlite3',
    }
}

# Configuración de validación de contraseñas
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

# Configuración de internacionalización
LANGUAGE_CODE = 'es'  # Idioma predeterminado: español
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = False

# Configuración de archivos estáticos (CSS, JavaScript, imágenes)
STATIC_URL = 'static/'

# Tipo de campo de clave primaria predeterminado
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Servidor de correo saliente de Gmail
EMAIL_USE_TLS = True
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')  # Tu dirección de correo electrónico de Gmail
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')  # Tu contraseña de Gmail (asegúrate de mantenerla segura)


TAILWIND_APP_NAME = 'theme'  # Especifica el nombre de la aplicación Tailwind

NPM_BIN_PATH = r"C:\Users\Breyner\AppData\Roaming\npm\npm.cmd"

INTERNAL_IPS = [
    "127.0.0.1",
]

