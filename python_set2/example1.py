import mysql.connector
conn = mysql.connector.connect(host='localhost',user='sain',password='ajaykasyap@2023')

if conn.is_connected():
    print("connection established....")
