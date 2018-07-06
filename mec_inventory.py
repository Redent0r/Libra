
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
 
def add_item_entry(connection,cursor,code = '#',name = "",quantity = 0,provider = "",costUni = 0.00,priceUniSug = 100 ,groupx = '',category = "",stockmin = "",stockmax = ""):
    """
        This function adds entries to the table Inventory and Entries.
    """
    cursor.execute('SELECT code,groupx FROM Inventory WHERE code=? AND groupx = ?',(code,groupx))
    data = cursor.fetchone()
    if data == None:
        transnum = ordinal_generator(connection,cursor)
        avail = quantity
        costItems = costUni * quantity
        costItems = round(costItems,2)
        priceUniSug = round(priceUniSug,2)
        costUni = round(costUni,2)
        b = (code,name,avail,costUni,priceUniSug,groupx,category,stockmin,stockmax)
        c = (transnum,code,name,quantity,provider,costUni,costItems,groupx,category)
        cursor.execute("INSERT INTO Inventory (code,name,avail,costUni,priceUniSug,groupx,category,stockmin,stockmax) VALUES(?,?,?,?,?,?,?,?,?)",b)
        cursor.execute("INSERT INTO Entries (dat,trans,code,name,quantity,provider,costUni,costItems,groupx,category) VALUES(date('now'),?,?,?,?,?,?,?,?,?)",c)
        connection.commit()
    else:         
        transnum = ordinal_generator(connection,cursor)
        avail = quantity
        costItems = costUni * quantity
        costItems = round(costItems,2)
        c = (transnum,code,name,quantity,provider,round(costUni,2),costItems,groupx,category)
    #-------------------------------------------------------------------------------------------------------
        increase_stock(cursor,code,groupx,quantity)
        update_all(cursor,code,groupx,costUni,priceUniSug,name,category) 
    #-------------------------------------------------------------------------------------------------------
        cursor.execute("INSERT INTO Entries (dat,trans,code,name,quantity,provider,costUni,costItems,groupx,category) VALUES(date('now'),?,?,?,?,?,?,?,?,?)",c)
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
def gen_query(cursor,table,column,stri,num):
    """
        Returns a list with elements that contain the string.
        Returns empty list if it does find one.
    """
    list1 = []
    list2 = []
    
    query = 'SELECT '+ str(column) +' FROM '+ str(table) 
    cursor.execute(query)
    data = cursor.fetchall()
    if (data == None):
        return list1
 
    for row in data:
        list1.append(row[0])
    for e in list1:
        if (stri in e ):
            list2.append(e)
 
    while (len(list2) > num):
        list2.pop()
    
    print(list2)
    return list2

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
 

def auto_del_0(connection,cursor):
    cursor.execute('SELECT avail FROM Inventory WHERE avail = 0')
    data4 = cursor.fetchone()
    if data4 != None:
        cursor.execute('DELETE FROM Inventory WHERE avail = 0')
 
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
 
def ordinal_generator(connection,cursor):
    """
        Generates string numbers starting with 1 and makes sure to never
        have used them before.It also adds them complementary 0's until it 
        has a minimum length of 8 characters.
    """
    exists = False
    trans = ""

    cursor.execute('SELECT MAX(ID) FROM OrdinalNumber')
    index = cursor.fetchone()
    if (index[0] == None):
        trans = '00000000'
    else:
        index = str(index[0])
        trans = index.zfill(8)
    d = ('a',)
    cursor.execute('INSERT INTO OrdinalNumber(num) VALUES (?)',d)
    connection.commit()
    return ('1' + trans)

def ordinal_generator2(connection,cursor):
    exists = False
    trans = ""

    cursor.execute('SELECT MAX(ID) FROM OrdinalNumberS')
    index = cursor.fetchone()
    if (index[0] == None):
        trans = '000000'
    else:
        index = str(index[0])
        trans = index.zfill(6)
    d = ('a',)
    cursor.execute('INSERT INTO OrdinalNumberS(num) VALUES (?)',d)
    connection.commit()
    return ('2' + trans)
    
 
def update_all(cursor,code,groupx,cost,price,name,category):
    t = (name,price,cost,category,code,groupx)
    cursor.execute('UPDATE Inventory SET name = ?,priceUniSug = ?,costUni = ?,category = ? WHERE code = ? AND groupx = ?',t)
     
def increase_stock(cursor,code,groupx,quantity):
    cursor.execute('SELECT avail FROM Inventory WHERE code = ? AND groupx = ?',(code,groupx))
    data = cursor.fetchone()
    avail = int(data[0]) + quantity
    cursor.execute('UPDATE Inventory SET avail = ? WHERE code = ? AND groupx = ?',(avail,code,groupx))
    return True

def decrease_stock(cursor,code,groupx,quant):
    #Reduce stock
    cursor.execute('SELECT avail FROM Inventory WHERE code = ? AND groupx = ?',(code,groupx))
    data = cursor.fetchone()
    avail = int(data[0]) - quant
    cursor.execute('UPDATE Inventory SET avail = ? WHERE code = ? AND groupx = ?',(avail,code,groupx))
    return True

def print_(cursor,table):#Print any table.
    cursor.execute('SELECT * FROM '+ table)
    data = cursor.fetchall()
    for row in data:
        print(row)
    return True

