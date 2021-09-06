import MySQLdb

try:
    query="create table cosmaticproduct(name varchar(50),price int(40))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="product")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    cur.execute(query)
    print("execute query")
    mycon.commit()
    print(query+"table created .... ")
except:
    print("table not created...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection close")