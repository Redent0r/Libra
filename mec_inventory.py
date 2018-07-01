
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
def calc_deb(cursor, date = None):
    """
        Calculates liquidity.
    """
    deb = []
    if (date == None):
        cursor.execute("SELECT priceItems FROM Outs WHERE payment = 'DEB'")
        data = cursor.fetchall()
        for e in data:
            deb.append(e[0])
    else:    
        cursor.execute("SELECT priceItems,dat FROM Outs WHERE payment = 'DEB'")
        data = cursor.fetchall()
        for e in data:
            if (date in e[1]):
                deb.append(e[0])
    deb = round(sum(deb),2)
    return deb

def calc_cre(cursor,date = None):
    """
        Calculates money customers currently owe.
    """
    cre = []
    if (date == None):
        cursor.execute("SELECT priceItems FROM Outs WHERE payment = 'CRE'")
        data = cursor.fetchall()
        for e in data:
            cre.append(e[0])
    else:    
        cursor.execute("SELECT priceItems,dat FROM Outs WHERE payment = 'CRE'")
        data = cursor.fetchall()
        for e in data:
            if (date in e[1]):
                cre.append(e[0])
    cre = round(sum(cre),2)
    return cre
 
#-------------------------------------------------------------------------------------------------------
def print_(cursor,table):#Print any table.
    cursor.execute('SELECT * FROM '+ table)
    data = cursor.fetchall()
    for row in data:
        print(row)
    return True