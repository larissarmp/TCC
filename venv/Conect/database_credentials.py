import petl as etl, psycopg2 as pg, sys
from sqlalchemy import *
import importlib


importlib.reload(sys)
dbConnection = { 'energia_dw':"dbname=energia_dw user=postgres host=127.0.0.0 password=1521 port=5432",
                 'energia_stage':"dbname=energia_stage user=postgres host=127.0.0.0 password=1521 port=5432"}

sourceConnetion = pg.connect(dbConnection['energia_dw'])
targetConnection = pg.connect(dbConnection ['energia_stage'])

sourceCursor = sourceConnection.cursor()
targetCursor = targetConnection.cursor()

sourceCursor.execute(""" SELECT table_name FROM information_schema.columns where table_name in ('nome')""")

sourceTables = sourceCursor.fetchall()

for t in sourceTables:
    targetConnection.execute('drop table if exists %s' % (t[0]))
    sourceDs = etl.fromdb(sourceConnection, "select * from test" %(t[0]))
    etl.todb(sourceConnection, targetConnection, t[0])