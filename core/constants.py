import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

RUN_ENV = os.environ.get('RUN_ENV')


if RUN_ENV == 'TEST':
    APP_SECRET_KEY = os.environ.get('SECRET_KEY_PROD') if os.environ.get(
        'SECRET_KEY_TEST') else ''
    DATABASE_URL = os.environ.get('DATABASE_URL_TEST') if os.environ.get('DATABASE_URL_TEST') else ''
    DEBUG_MODE = True

elif RUN_ENV == 'PROD':
    APP_SECRET_KEY = os.environ.get('SECRET_KEY_PROD') if os.environ.get(
        'SECRET_KEY_PROD') else ''
    DATABASE_URL = os.environ.get('DATABASE_URL_PROD') if os.environ.get(
        'DATABASE_URL_PROD') else ''
    DEBUG_MODE = False
    
else:
    APP_SECRET_KEY = os.environ.get('SECRET_KEY_LOCAL') if os.environ.get(
        'SECRET_KEY_LOCAL') else 'print("No secret key found")'
    DATABASE_URL = os.environ.get('DATABASE_URL_LOCAL') if os.environ.get('DATABASE_URL_LOCAL') else ''  
    DEBUG_MODE = True  
    
    

  