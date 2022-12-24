#!/usr/bin/python3
"""a module that lists all states with a name starting with N
   from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, password="kamau2368",
                         user="root", database="hbtn_0e_0_usa")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    for row in cursor.fetchall():
        print('{}'.format(row))
    cursor.close()
    db.close()
