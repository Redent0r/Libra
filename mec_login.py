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

def check_login(cursor,username,password):# Logs in ,returns current user.
    a = (username,password,)
    cursor.execute("SELECT User,Pass FROM login WHERE User = ? AND Pass = ?",a)
    data = cursor.fetchone()#Returns a single tuple.
    if data == None:#f returns type None.
        print("Not registered")
        return False
    return True     

def print_login_table(cursor):
    elems = cursor.execute("SELECT * FROM login")
    data = cursor.fetchall()
    for row in data:
        print(row)
def check_if_admin(cursor,username):
    a =(username,)
    cursor.execute("SELECT class FROM login WHERE User = ?",a)
    data = cursor.fetchone()
    if data == None:
        return False
    elif data[0] == 'admin':
        return True
    else:
        return False
def remove_user():
    pass

def log_out(cursor,connection):
    print('')
    print('.................Closing')
    connection.commit()
    cursor.close()
    sys.exit()
    
