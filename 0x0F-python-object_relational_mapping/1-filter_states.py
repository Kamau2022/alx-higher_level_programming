#!/usr/bin/python3
"""a module that lists all states with a name starting with N
   from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, password=argv[1],
                         user=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    for row in cursor.fetchall():
        print('{}'.format(row))
    cursor.close()
    db.close()
