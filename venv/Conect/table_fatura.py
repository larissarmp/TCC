import petl as etl, psycopg2 as pg, sys
from sqlalchemy import *

dbConnection = { 'energia_stage':"dbname=energia_stage user=postgres host=localhost password=1521 port=5432",
                 'energia_dw':"dbname=energia_dw user=postgres host=localhost password=1521 port=5432"}

sourceConnection = pg.connect(dbConnection['energia_stage'])
targetConnection = pg.connect(dbConnection ['energia_dw'])

sourceCursor = sourceConnection.cursor()
targetCursor = targetConnection.cursor()

sourceCursor.execute(""" SELECT table_name FROM information_schema.columns where table_name in ('sideufg_fatura','sideufg_juros_fatura')""")

sourceTables = sourceCursor.fetchall()

for t in sourceTables:

    fatura = etl.join('sideufg_fatura', 'sideufg_juros_fatura')

