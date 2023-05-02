import cx_Oracle
conn=cx_Oracle.connect('system/ajaykasyap//localhost:1521/xe')
print(conn.version)
