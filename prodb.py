import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    password='MissZesty@7320',
    user='root'
    )

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE prodb')

print("Database 'prodb' created successfully.")
