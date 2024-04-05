import mysql.connector

 

connection = mysql.connector.connect(
    user = 'root',
    database = 'bankapp',
    password = '0saeAnnett3'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM accounts")
cursor.execute(testQuery) 

for item in cursor:
    print(item)

 
cursor.close()
connection.close()