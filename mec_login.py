"""
    Author:Christopher Holder
    Project : Version 1.0(Login)
"""
import sqlite3
import sys

def create_login_table(cursor,connection):#Creates login table.
    cursor.execute("CREATE TABLE IF NOT EXISTS login(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, User TEXT NOT NULL, Pass TEXT NOT NULL,class TEXT NOT NULL,dat TEXT);")
    cursor.execute("SELECT User FROM login WHERE User = 'Administrator'")
    data = cursor.fetchone()
    
    if data == None:
        print("...............Adding admin account")
        cursor.execute("INSERT INTO login (User, Pass,class,dat)""VALUES ('Administrator','nimda','admin',date('now'))")
        print("...............Account added")
    connection.commit()
    return True
