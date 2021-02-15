import os
from django.utils.translation import ugettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es'
# Lista de activados
DEFAULT_LANGUAGE = 1  # el primero en la lista
LANGUAGES = (
    ('es', _('Spanish')),
    ('br', _('Brazil')),
    ('en', _('English')),
)

TIME_ZONE = 'America/La_Paz'
USE_I18N = True
USE_L10N = True
USE_TZ = True