MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # libreria para deploy debug false
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # crum
    'crum.CurrentRequestUserMiddleware'
]
#
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#
