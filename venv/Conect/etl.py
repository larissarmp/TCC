import psycopg2
from petl import look, fromdb
connection = psycopg2.connect("dbname=energia_dw user=postgres host=localhost password=1521 port=5432")
table =fromdb(connection, 'select name from test')
look(table)