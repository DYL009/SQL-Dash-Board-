import mysql.connector
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user = 'root',
        password = '',
        database='indigo'
    )
    mycursor = conn.cursor()
    print('Connection established')
except:
    print('Connection error')

# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()
#  craeety table

# mycursor.execute("""
# CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL ) """)
# conn.commit()

# Insert data to the table
# mycursor.execute("""
#     INSERT INTO airport VALUES
#     (1,'DEL','New Delhi','IGIA'),
#     (2,'CCU','Kolkata','NSCA'),
#     (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()

#search 
mycursor.execute('select*from airport where airport_id>1')
data=mycursor.fetchall()
print(data)
for i in data:
    print(i[3])

#update
mycursor.execute("""update airport 
                 set name='Bombay'
                 where airport_id=3
""")
conn.commit()

#search 
mycursor.execute('select*from airport where airport_id>1')
data=mycursor.fetchall()
print(data)

#delete 
mycursor.execute("delete from airport where airport_id=3")
conn.commit()
mycursor.execute('select*from airport where airport_id')
data=mycursor.fetchall()
print(data) 