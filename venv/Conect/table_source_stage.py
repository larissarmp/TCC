import petl as etl, psycopg2 as pg, sys
from sqlalchemy import *
import importlib


importlib.reload(sys)
dbConnection = { 'sideufg_db':"dbname=sideufg_db user=larissa host=200.137.220.157 password=pamonha&cafe port=5432",
                 'energia_stage':"dbname=energia_stage user=postgres host=localhost password=1521 port=5432"}

sourceConnection = pg.connect(dbConnection['sideufg_db'])
targetConnection = pg.connect(dbConnection ['energia_stage'])

sourceCursor = sourceConnection.cursor()
targetCursor = targetConnection.cursor()

sourceCursor.execute(""" SELECT table_name FROM information_schema.columns where table_name in ('sideufg_adicional_fatura',
                        'sideufg_dado_fatura', 'sideufg_endereco','sideufg_fatura','sideufg_juros_fatura',
                        'sideufg_multa_fatura')""")

sourceTables = sourceCursor.fetchall()

for t in sourceTables:
    targetCursor.execute('drop table if exists %s' % (t[0]))
    sourceDs = etl.fromdb(sourceConnection, "select * from %s" %(t[0]))
    etl.todb(sourceDs, targetConnection, t[0], create=True, sample=1000000)