#!/usr/bin/python3
"""a module that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    db=MySQLdb.connect(
    host="localhost",
    port =3307, 
    password ="kamau2368", 
    user="root", 
    database="hbtn_0e_0_usa"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        print (row[0], row[1])
    cursor.close()
    db.close()
