import petl as etl, psycopg2 as pg, sys
from sqlalchemy import *
import importlib


importlib.reload(sys)
dbConnection = { 'sideufg_db':"dbname=sideufg_db user=larissa host=200.137.220.157 password=pamonha&cafe",
                 'energia_stage':"dbname=energia_stage user=postgres password=1521"}

sourceConnetion = pg.connect(dbConnection['sideufg_db'])
targetConnection = pg.connect(dbConnection ['energia_stage'])

sourceCursor = sourceConnection.cursor()
targetCursor = targetConnection.cursor()

sourceCursor.execute(""" SELECT *
FROM public.sideufg_adicional_fatura""")

sourceTables = sourceCursor.fetchall()

for t in sourceTables:
    # targetConnection.execute('drop table if exists %s' % (t[0]))
    sourceDs = etl.fromdb(sourceConnection, "select * from sideufg_adicional_fatura")
    etl.todb(sourceConnection, targetConnection, t[0])