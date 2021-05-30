import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=dbserver;'
                      'Database=db;'
                      'UID=user;'
                    'PWD=pwd;')

cursor = conn.cursor()
cursor.execute('SELECT top 10 * FROM table order by id desc')

for row in cursor:
    print(row)