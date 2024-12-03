import mysql.connector
mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "spectrum",
    database="marifs"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE unique_ideas (name varchar (100),address varchar(100))")
# sql= "INSERT INTO unique_ideas(name ,address) VALUES (%s,%s)"
# val=[
#     ("Arif","TVM,KZK"),
#     ("Ashish","Alappuzha,chengannur"),
#     ("Anila","Alappuzha,KYLM")
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

sql="UPDATE unique_ideas set address ='Uganda' WHERE address = 'Alappuzha,KYLM'"
mycursor.execute(sql)

mydb.commit()

