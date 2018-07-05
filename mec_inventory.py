
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

def query_add(cursor,code,groupx):
    cursor.execute('SELECT name,costUni,priceUniSug,category,stockmin,stockmax FROM Inventory WHERE code = ? AND groupx = ?',(code,groupx))
    data = cursor.fetchone()
    if (data == None):
        return False
    return data

#-------------------------------------------------------------------------------------------------------
def calc_bal_his(cursor):
    """
        CalcuLates balances of all exits and entries ever and adds them to the historic balance db.
    """
    t = []
    cursor.execute('SELECT costItems FROM Entries')
    data = cursor.fetchall()
    for row0 in data:
        t.append(row0[0])
    costTot = sum(t)

    cursor.execute('SELECT priceItems,revenue,tax,winnings FROM Outs')
    query = cursor.fetchall()
    
    #-------------------------------------------------------------------------------------------------------

    p = []
    for row2 in query:
        p.append(row2[0])
    priceTot = sum(p)
    #-------------------------------------------------------------------------------------------------------
    g = []
    for row3 in query:
        g.append(row3[1])
    revenueTot = sum(g)
    #-------------------------------------------------------------------------------------------------------
    i = []
    for row4 in query:
        i.append(row4[2])
    taxTot = sum(i)
    #-------------------------------------------------------------------------------------------------------
    x = []
    for row5 in query:
        x.append(row5[3])
    winningsTot = sum(x)
    #-------------------------------------------------------------------------------------------------------
    cd = calc_deb(cursor)
    cc = calc_cre(cursor)   

    return [costTot,priceTot,cd,cc,round((priceTot - costTot),2),taxTot,round((priceTot - costTot - taxTot),2)]
 
def calc_bal_mes(cursor,year,month):

    if (len(year) != 4) or (int(year) < 2016) or (int(year)> 3000) or (isinstance(year,float)) or (len(month) != 2)  or (isinstance(month,float)) or (int(month)< 0) or (int(month)>12) :
        print('Bad date')
        return False
    date = year+'-'+ month
    entries = []

    #-------------------------------------------------------------------------------------------------------
    cursor.execute('SELECT dat,costItems FROM Entries')
    data = cursor.fetchall()
    for row in data:
        if (date in row[0]):
            entries.append(row[1])
    costTot = sum(entries)

    cursor.execute('SELECT dat,priceItems,revenue,tax,winnings FROM Outs ')
    query = cursor.fetchall()
    #-------------------------------------------------------------------------------------------------------
    p = []
    for e in query:
        if (date in e[0]):
            p.append(e[1])
    priceTot = sum(p)
    #-------------------------------------------------------------------------------------------------------
    g = []
    for d in query:
        if (date in d[0]):
            g.append(d[2])
    revenueTot = sum(g)
    #-------------------------------------------------------------------------------------------------------
    i = []
    for elem in query:
        if (date in elem[0]):
            i.append(elem[3])
    taxTot = sum(i)
    #-------------------------------------------------------------------------------------------------------
    x = []
    for al in query:
        if(date in al[0]):
            x.append(al[4])
    winningsTot = sum(x)
    #-------------------------------------------------------------------------------------------------------
    cd = calc_deb(cursor,date)
    cc = calc_cre(cursor,date)
 
    return [costTot,priceTot,cd,cc,round((priceTot - costTot),2),taxTot,round((priceTot - costTot - taxTot),2)]
      
def calc_bal_year(cursor,year):

    if (len(year) != 4) or (int(year) < 2016) or (int(year)> 3000) or (isinstance(year,float)) :
        print('Not proper date.')
        return False
    date = year 
    entries = []
     #-------------------------------------------------------------------------------------------------------
    cursor.execute('SELECT dat,costItems FROM Entries')
    data = cursor.fetchall()
    for row in data:
        if (date in row[0]):
            entries.append(row[1])
    costTot = sum(entries)

    cursor.execute('SELECT dat,priceItems,revenue,tax,winnings FROM Outs ')
    query = cursor.fetchall()
    #-------------------------------------------------------------------------------------------------------
    p = []
    for e in query:
        if (date in e[0]):
            p.append(e[1])
    priceTot = sum(p)
    #-------------------------------------------------------------------------------------------------------
    g = []
    for d in query:
        if (date in d[0]):
            g.append(d[2])
    revenueTot = sum(g)
    #-------------------------------------------------------------------------------------------------------
    i = []
    for elem in query:
        if (date in elem[0]):
            i.append(elem[3])
    taxTot = sum(i)
    #-------------------------------------------------------------------------------------------------------
    x = []
    for al in query:
        if(date in al[0]):
            x.append(al[4])
    winningsTot = sum(x)
    #-------------------------------------------------------------------------------------------------------
    cd = calc_deb(cursor,date)
    cc = calc_cre(cursor,date)
 
    return [costTot,priceTot,cd,cc,round((priceTot - costTot),2),taxTot,round((priceTot - costTot - taxTot),2)]

def calc_bal_day(cursor,year,month,day):

    if (len(year) != 4) or (int(year) < 2016) or (int(year)> 3000) or (isinstance(year,float)) or (len(month) != 2)  or (isinstance(month,float)) or (int(month)< 0) or (int(month)>12) or (int(day) > 31) or (len(day) != 2):
        print('Bad date')
        return False
    date = year+'-'+ month + '-' + day
    
    entries = []
    cursor.execute('SELECT dat,costItems FROM Entries')
    data = cursor.fetchall()
    for row in data:
        if (date in row[0]):
            entries.append(row[1])
    costTot = sum(entries)

    cursor.execute('SELECT dat,priceItems,revenue,tax,winnings FROM Outs ')
    query = cursor.fetchall()
    #-------------------------------------------------------------------------------------------------------
    p = []
    for e in query:
        if (date in e[0]):
            p.append(e[1])
    priceTot = sum(p)
    #-------------------------------------------------------------------------------------------------------
    g = []
    for d in query:
        if (date in d[0]):
            g.append(d[2])
    revenueTot = sum(g)
    #-------------------------------------------------------------------------------------------------------
    i = []
    for elem in query:
        if (date in elem[0]):
            i.append(elem[3])
    taxTot = sum(i)
    #-------------------------------------------------------------------------------------------------------
    x = []
    for al in query:
        if(date in al[0]):
            x.append(al[4])
    winningsTot = sum(x)
    #-------------------------------------------------------------------------------------------------------
    cd = calc_deb(cursor,date)
    cc = calc_cre(cursor,date)

 
    return [costTot,priceTot,cd,cc,round((priceTot - costTot),2),taxTot,round((priceTot - costTot - taxTot),2)]
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
def unique(cursor,column,table,key_column = "",key = ""):
    if key_column == "":
        cursor.execute("SELECT DISTINCT "+ column + " FROM " + table)
    else:
        cursor.execute("SELECT DISTINCT " + column + " FROM " + table + " WHERE " + key_column + " = ?",(key,))
    unique_values = []
    data = cursor.fetchall()
    if data != None:
        for line in data:
            unique_values.append(line[0])
    return unique_values
#-------------------------------------------------------------------------------------------------------
def update_all(cursor,code,groupx,cost,price,name,category):
    t = (name,price,cost,category,code,groupx)
    cursor.execute('UPDATE Inventory SET name = ?,priceUniSug = ?,costUni = ?,category = ? WHERE code = ? AND groupx = ?',t)
     
def increase_stock(cursor,code,groupx,quantity):
    cursor.execute('SELECT avail FROM Inventory WHERE code = ? AND groupx = ?',(code,groupx))
    data = cursor.fetchone()
    avail = int(data[0]) + quantity
    cursor.execute('UPDATE Inventory SET avail = ? WHERE code = ? AND groupx = ?',(avail,code,groupx))
    return True

def print_(cursor,table):#Print any table.
    cursor.execute('SELECT * FROM '+ table)
    data = cursor.fetchall()
    for row in data:
        print(row)
    return True