import mysql.connector

cnx = mysql.connector.connect(user='nivedha', password='nivedha',
                              host='34.77.119.137',
                              port=3306,
                              database='placement')
cnx.close()