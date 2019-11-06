import pandas as pd
import petl as etl, psycopg2 as pg, sys
from sqlalchemy import *

dbConnection = { 'energia_stage':"dbname=energia_stage user=postgres host=localhost password=1521 port=5432"}

Fatura_df = pd.read_sql('fatura', con=dbConnection)
pd.merge(sideufg_juros_fatura, Fatura_df, left_on='name', right_on='title')
pd.DataFrame.to_sql(fatura, dbConnection)
