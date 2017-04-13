SECRET_KEY = ')%j71x_*dfgdfgf*@yhggyj59puq@4z7zdfgdfgdf)^@snm1fdgdfg&gn$0kqn5dfgdgr4hrqfl)sadcf'
ADMINS = (
     ('TAksenov', 'taksenov@gmail.com'),
)
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME':     'www__base',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER':     'qduser',
        'PASSWORD': 'poi4vtyz',
        'HOST':     'mysql',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT':     '',
        'OPTIONS': {'charset': 'utf8mb4'}                     # Set to empty string for default.
    }
}
