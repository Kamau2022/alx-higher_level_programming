#!/usr/bin/python3
"""a module that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, password=argv[1],
                         user=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities LEFT JOIN states\
                    ON cities.state_id = states.id\
                    ORDER by cities.id")
    for row in cursor.fetchall():
        print('{}'.format(row))
    cursor.close()
    db.close()
