"""
    Author:Christopher Holder
    Project : Version 1.0(Login)
"""
import sqlite3
import sys

#Creates login table in the database
def create_login_table(cursor,connection):
    cursor.execute("CREATE TABLE IF NOT EXISTS login(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, User TEXT NOT NULL, Pass TEXT NOT NULL,class TEXT NOT NULL,dat TEXT);")
    cursor.execute("SELECT User FROM login WHERE User = 'Administrator'")
    data = cursor.fetchone()
    
    if data == None:
        print("...............Adding admin account")
        cursor.execute("INSERT INTO login (User, Pass,class,dat)""VALUES ('Administrator','nimda','admin',date('now'))")
        print("...............Account added")
    connection.commit()
    return True

def check_login(cursor,username,password):# Logs in ,returns current user.
    a = (username,password,)
    cursor.execute("SELECT User,Pass FROM login WHERE User = ? AND Pass = ?",a)
    data = cursor.fetchone()#Returns a single tuple.
    if data == None:# returns type None.
        print("Combination does not matches")
        return False
    return True     
