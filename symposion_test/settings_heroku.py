import dj_database_url
from .settings import *

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# # STATIC
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# STATIC_URL = '/static/'
#
# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'