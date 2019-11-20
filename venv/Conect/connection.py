import pandas as pd
from sqlalchemy import create_engine


def connection(engine):
    DATABASES = {
        'energia_stage': {
            'NAME': 'energia_stage',
            'USER': 'postgres',
            'PASSWORD': '1521',
            'HOST': 'localhost',
            'PORT': 5432,
        },
    }

    # choose the database to use
db = DATABASES['energia_stage']

# construct an engine connection string
engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user=db['USER'],
    password=db['PASSWORD'],
    host=db['HOST'],
    port=db['PORT'],
    database=db['NAME'],
)
engine = create_engine(engine_string)

def connection(engine):
    DATABASES = {
        'sideufg_db': {
            'NAME': 'sideufg_db',
            'USER': 'larissa',
            'PASSWORD': 'pamonha&cafe',
            'HOST': '200.137.220.157',
            'PORT': 5432,
        },
    }

    # choose the database to use
    db = DATABASES['sideufg_db']

    # construct an engine connection string
    engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
        user=db['USER'],
        password=db['PASSWORD'],
        host=db['HOST'],
        port=db['PORT'],
        database=db['NAME'],
    )
    engine = create_engine(engine_string)