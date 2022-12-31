#!/usr/bin/python3
""" a script that takes in an argument and displays all values 
    in the states table of hbtn_0e_0_usa where name matches the argument.
"""

def getStates(userName, passWord, dbName, statename):
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, password=password,
                         user=user, database=data)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(statename))
    for row in cursor.fetchall():
        print('{}'.format(row))
    cursor.close()
    db.close()
if __name__ == "__main__":
    """ Take in arguments and passes to get states from db """
    from sys import argv

    getStates(argv[1], argv[2], argv[3], argv[4])
