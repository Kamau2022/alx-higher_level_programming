#!/usr/bin/python3
""" a script that takes in an argument and displays all values 
    in the states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    if len(argv) != 5:
        print("Usage: {} username password database_name".format(argsv[0]))
        exit(1)
    username = "root"
    password = "kamau2368"
    data = argv[3]
    statename = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, password=argv[1],
                         user=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(statename))
    for row in cursor.fetchall():
        print('{}'.format(row))
    cursor.close()
    db.close()
