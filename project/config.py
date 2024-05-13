from decouple import config
from dj_database_url import parse as db_url

DEBUG=config('DEBUG', cast=bool, default=False)
SECRET_KEY = config('SECRET_KEY')

DATABASE_URL=config('DATABASE_URL', default='sqlite:///:memory:', cast=db_url)
DATABASE_URL_SC=config('DATABASE_URL_SC', default='sqlite:///:memory:', cast=db_url)

DATABASE_URL["OPTIONS"]={
    'options':config('DATABASE_OPTIONS')
}