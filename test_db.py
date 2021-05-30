import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LON6UTHPISQL01.stg.mkapp.net;'
                      'Database=Maipprocessing;'
                      'UID=HPI_UT_APP_USER;'
                    'PWD=WZWvgb9EqU;')

cursor = conn.cursor()
cursor.execute('SELECT top 10 * FROM maipprocessing.dbo.execution_status order by id desc')

for row in cursor:
    print(row)