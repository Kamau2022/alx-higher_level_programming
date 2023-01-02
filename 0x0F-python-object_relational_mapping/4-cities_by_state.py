#!/usr/bin/python3
"""a module that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, password="kamau2368",
                         user="root", database="hbtn_0e_4_usa")
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities INNER JOIN states\
                    ON cities.state_id = states.id\
                    ORDER by cities.id")
    for row in cursor.fetchall():
        print('{}'.format(row))
    cursor.close()
    db.close()
