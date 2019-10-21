import pyodbc

cnxn = pyodbc.connect(
    'DRIVER={Devart ODBC Driver for PostgreSQL};Server=myserver;Port=myport;Database=mydatabase;User ID=myuserid;Password=mypassword;String Types=Unicode')

cursor = cnxn.cursor()
cursor.execute("SELECT ShipName, ShipCity FROM Orders WHERE ShipCountry = 'USA'")
rows = cursor.fetchall()
for row in rows:
    print(row.ShipName, row.ShipCity)