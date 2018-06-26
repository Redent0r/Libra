
"""
    Author:Christopher Holder
"""
def create_tables(connection,cursor):
    """
        This function creates the neccessary tables in the database.
    """
    cursor.execute("CREATE TABLE IF NOT EXISTS OrdinalNumber(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,num TEXT NOT NULL)")
 
    cursor.execute('CREATE TABLE IF NOT EXISTS OrdinalNumberS(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, num TEXT NOT NULL)')
 
    cursor.execute("""CREATE TABLE IF NOT EXISTS Inventory(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,code TEXT NOT NULL,name TEXT NOT NULL,avail INTEGER NOT NULL,costUni REAL NOT NULL,priceUniSug REAL NOT NULL,groupx TEXT NOT NULL,category TEXT,stockmin INTEGER,stockmax INTEGER)""")
 
    cursor.execute("""CREATE TABLE IF NOT EXISTS Entries(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,dat TEXT,trans TEXT,code TEXT NOT NULL,name TEXT NOT NULL,quantity INTEGER NOT NULL,provider TEXT ,costUni REAL NOT NULL,costItems REAL NOT NULL,groupx TEXT NOT NULL, category TEXT)""") 
 
    cursor.execute("""CREATE TABLE IF NOT EXISTS Outs(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,dat TEXT,trans TEXT,code TEXT NOT NULL,name TEXT NOT NULL,quantity INTEGER NOT NULL,groupx TEXT NOT NULL,priceUni REAL,priceItems REAL,tax REAL,revenue REAL,winnings REAL,payment TEXT,client TEXT)""")

    connection.commit()
    return True
 
#-------------------------------------------------------------------------------------------------------
def print_(cursor,table):#Print any table.
    cursor.execute('SELECT * FROM '+ table)
    data = cursor.fetchall()
    for row in data:
        print(row)
    return True