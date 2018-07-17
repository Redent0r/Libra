
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
 
    cursor.execute('CREATE TABLE IF NOT EXISTS Clients(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,identification TEXT,name TEXT,mail TEXT,num TEXT,cel TEXT,fax TEXT ,direction TEXT,bought INTEGER,money_invested REAL,paid REAL,debt REAL)')

    add_client(connection,cursor,'Misc','','','','','','')
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

def add_item_exit_fixed(connection,cursor,code = "#",quantity = 1,tax = 0.07,pricef = 10.00,discount = 0,payment = 'CRE',client = '',trans='',groupx = ''):
     
    a =(code,groupx)
    cursor.execute('SELECT name FROM Inventory WHERE code = ? AND groupx = ?',a)
    data0 = cursor.fetchone()
    name = str(data0[0])
    decrease_stock(cursor,code,groupx,quantity)
    priceUni = pricef
    taxTot = tax * priceUni * quantity
    taxTot = round(taxTot,2)
    priceItems = priceUni * (tax + 1) * quantity
    if (discount == 0):
        priceItems = round(priceItems,2)
    else:
        discount = priceItems * discount
        priceItems = priceItems - discount
        priceItems = round(priceItems,2)
    cursor.execute('SELECT costUni FROM Inventory WHERE code = ? AND groupx = ?',a)
    data2 = cursor.fetchone()
    costItems = (float(data2[0]))* quantity
    costItems = round(costItems,2)
    revenue = priceItems - costItems 
    revenue = round(revenue,2)
    winnings = revenue - taxTot
    winnings = round(winnings,2)

    auto_del_0(connection,cursor)
    
    b = (trans,code,name,quantity,groupx,priceUni,priceItems,taxTot,revenue,winnings,payment,client)
    cursor.execute("INSERT INTO Outs (dat,trans,code,name,quantity,groupx,priceUni,priceItems,tax,revenue,winnings,payment,client) VALUES(date('now'),?,?,?,?,?,?,?,?,?,?,?,?)",b)
    update_client_info(connection,cursor,client)
    connection.commit()
    #-------------------------------------------------------------------------------------------------------
    return True
#-------------------------------------------------------------------------------------------------------
def modify(connection,cursor,code,groupx,avail,priceUni,category,smin,smax,costUni, name):
    if (groupx == 'Global'):
        cursor.execute('UPDATE Inventory SET name = ?,priceUniSug = ?,category = ?, stockmin = ?,stockmax = ? ,costUni = ? WHERE code = ?',(name,priceUni,category,smin,smax,costUni,code))
    else:
        cursor.execute('UPDATE Inventory SET name = ?,avail = ?,priceUniSug = ?,category = ?, stockmin = ?,stockmax = ? ,costUni = ? WHERE code = ? AND groupx = ?',(name,avail,priceUni,category,smin,smax,costUni,code,groupx))
    connection.commit()

def modify_client(connection,cursor,name,identification,mail,num,cel,fax,direction):
    sel = (identification,mail,num,cel,fax,direction,name)
    cursor.execute('UPDATE Clients SET identification = ?,mail = ?,num = ?,cel = ?,fax = ?,direction = ? WHERE name = ?',sel)
    connection.commit()
   

def shopping_cart(connection,cursor,lista):
    """
    This function does multiple sales.lista is a list of lists.
    The elements should contain the following arguments. : [code,quantity,tax,pricef,discount,payment,client,groupx]
    """
    counter = 0
    results =[]
    failed = {}
    for e in lista:
        a = sale_valid2(cursor,e[0],e[1],e[7])
        results.append(a)
    for el in range(len(results)):
        if (results[el] != 0):
            failed.setdefault((el+1),results[el])
         
    if (len(failed) > 0):
        print(failed)
        return failed
    t = ordinal_generator2(connection,cursor)    
    for e in lista:
        counter += 1
        transa = t + (str(counter).zfill(3))
        add_item_exit_fixed(connection,cursor,e[0],e[1],e[2],e[3],e[4],e[5],e[6],transa,e[7])
 
    return True
 
 
def sale_valid(cursor,code,client_name,quantity,groupx):
    """
    Checks If client ,quantity, or code exists.
    0 = Sucessful
    1 = does not exists. 2 = reduces below existing units ,
    3 = client does not exist
 
    """    
    l = []
    a = (code,groupx)
    b = (client_name,)
    cursor.execute('SELECT code,avail FROM Inventory WHERE code = ? AND groupx = ?',a)
    data0 = cursor.fetchone()
    if (data0 == None):
        l.append(1)
    if (data0 != None):
        if (data0[1] < quantity):
            l.append(2)
            
   
    cursor.execute('SELECT name FROM Clients WHERE name = ?',b)
    data2 = cursor.fetchone()
    if (data2 == None):
        l.append(3)
 
    if (len(l) == 0):
        l = 0
 
    return l

def sale_valid2(cursor,code,quantity,groupx):
    """
    Checks If client ,quantity, or code exists.
    0 = Sucessful
    1 = does not exists. 2 = reduces below existing units ,
 
    """    
    l = []
    a = (code,groupx)
    cursor.execute('SELECT code,avail FROM Inventory WHERE code = ? AND groupx = ?',a)
    data0 = cursor.fetchone()
    if (data0 == None):
        l.append(1)
    if (data0 != None):
        if (data0[1] < quantity):
            l.append(2)
    
    if (len(l) == 0):
        l = 0
 
    return l

def query_add(cursor,code,groupx):
    cursor.execute('SELECT name,costUni,priceUniSug,category,stockmin,stockmax FROM Inventory WHERE code = ? AND groupx = ?',(code,groupx))
    data = cursor.fetchone()
    if (data == None):
        return False
    return data

def query_sale(cursor,code,groupx):
    """
        Returns list with [name,priceUniSug,costUni]
    """
    cursor.execute('SELECT name,priceUniSug,costUni FROM Inventory WHERE code = ? AND groupx = ?',(code,groupx))
    data = cursor.fetchone()
    if (data == None):
        print('No name with that code')
        return False

    return data 

def query_modify(cursor,code,groupx):
    """
         Returns [avail,priceUniSug,costUni,category,stockmin,stockmax,name]
    """
    cursor.execute('SELECT avail,priceUniSug,costUni,category,stockmin,stockmax, name FROM Inventory WHERE code = ? AND groupx = ?',(code,groupx))
    data = cursor.fetchone()
    return data

def query_client(cursor,name):
    """
        Returns [identification,mail,num,cel,fax,direction,bought,money_invested,paid,debt]
    """
    cursor.execute('SELECT identification,mail,num,cel,fax,direction FROM Clients WHERE name = ?',(name,))
    data = cursor.fetchone()
    return data

#-------------------------------------------------------------------------------------------------------
 
def add_client(connection,cursor,identification,name,mail,num,cel,fax,direction):
    """
        Adds client to client table.
        Returns False if the name has been used before.
    """
    bought = 0
    money_invested = 0.0
    paid = 0.0
    debt = 0.0
    i = (name,)
    cursor.execute('SELECT name FROM Clients WHERE name = ?',i)
    data = cursor.fetchone()
    if (data != None):
        print('Name already used.')
        return False
    t = (identification,name,mail,num,cel,fax,direction,bought,money_invested,paid,debt)
    cursor.execute("INSERT INTO Clients (identification,name,mail,num,cel,fax,direction,bought,money_invested,paid,debt) VALUES (?,?,?,?,?,?,?,?,?,?,?)",t)
    connection.commit()
    return True
 
 
def update_client_info(connection,cursor,user):

    a = (user,)
    money = []
    articles = []
    cursor.execute('SELECT priceItems,quantity FROM Outs WHERE client = ? ',a)
    data2 = cursor.fetchall()
    if (data2 == None):
        return False
    for row2 in data2:
        money.append(row2[0])
    for row2 in data2:
        articles.append(row2[1])
    debit = []
    credit = []
    cursor.execute("SELECT priceItems FROM Outs WHERE client = ? AND payment = 'DEB'",a)
    data4 = cursor.fetchall()
    for row4 in data4:
        debit.append(row4[0])
        
    cursor.execute("SELECT priceItems FROM Outs WHERE client = ? AND payment = 'CRE'",a)
    data5 = cursor.fetchall()
    for row5 in data5:
        credit.append(row5[0])
 
    money = sum(money)
    articles = sum(articles)
    debit = sum(debit)
    credit =sum(credit)
 
    cursor.execute('UPDATE Clients SET bought = ?,money_invested = ?,paid = ?,debt = ? WHERE name = ?',(articles,money,debit,credit,user))

    connection.commit()
     

def del_client_id(connection,cursor,identification):
    cursor.execute('DELETE FROM Clients WHERE identification = ?',(identification,))
    connection.commit()
    return True


def del_client_name(connection,cursor,name):
    cursor.execute('DELETE FROM Clients WHERE name = ?',(name,))
    connection.commit()
    return True
     
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
 
def paid(connection,cursor,trans):
    """
        Marks an item as paid.
    """
    t = (trans,)
    cursor.execute("UPDATE Outs SET payment = 'DEB' WHERE trans = ?",(trans,))
    cursor.execute("SELECT client FROM Outs WHERE trans = ?",(trans,))
    data = cursor.fetchone()
    update_client_info(connection,cursor,data[0])
    connection.commit()
 
def move_to_credit(connection,cursor,trans):
    """
        Marks an item as not paid.
    """
    cursor.execute("UPDATE Outs SET payment = 'CRE' WHERE trans = ?",(trans,))
    cursor.execute("SELECT client FROM Outs WHERE trans = ?",(trans,))
    data = cursor.fetchone()
    update_client_info(connection,cursor,data[0])
    connection.commit()
 
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
 
def del_general(connection,cursor,trans):
    """
        Generalizes use of delete function.
        Clients table delete not included.
    """
    try:
        if(trans[0] == '1'):
            return del_item_entries(connection,cursor,trans)
        elif(trans[0] == '2'):
            return del_item_salidas(connection,cursor,trans)
        else:
            print('Unknown transaction number')
            return False
 
    except TypeError:
        print('Error in cell')
        return False

def del_item_entries(connection,cursor,trans):
    """
        Deletes items from entries by transaction number.
    """
    cursor.execute('DELETE FROM Entries WHERE trans = ?',(trans,))
    connection.commit()
    return True
def del_item_inventory(connection,cursor,code,groupx):
    """
        Deletes items from inventory by code.
    """
    cursor.execute('DELETE FROM Inventory WHERE code = ? AND groupx = ?',(code,groupx))
    connection.commit()
    return True
def del_item_salidas(connection,cursor,trans):
    """
        Deletes items by transaction number.
    """
    cursor.execute('SELECT quantity FROM Outs WHERE trans = ?',(trans,))
    data = cursor.fetchone()
    if (data == None):
        print('Transaction number not from an Out')
        return False
    cursor.execute('SELECT priceItems,client FROM Outs WHERE trans = ?',(trans,))
    p = cursor.fetchone()
    cursor.execute('SELECT money_invested FROM Clients WHERE name = ? ',(p[1],))
    d = cursor.fetchone()
    f = d[0]- p[0]
    cursor.execute('UPDATE Clients SET money_invested = ? WHERE name = ?',(f,p[1]))

    cursor.execute('SELECT code,groupx FROM Outs WHERE trans = ?',(trans,))
    data2 = cursor.fetchone()
    #-------------------------------------------------------------------------------------------------------
    g = (data2[0],data2[1])
    cursor.execute('SELECT avail FROM Inventory WHERE code = ? AND groupx = ?',g)
    data3 = cursor.fetchone()
    avail = data3[0] + data[0]
    b =(avail,data2[0],data2[1])
    cursor.execute('UPDATE Inventory SET avail = ? WHERE code = ? AND groupx = ?',b)
    #-------------------------------------------------------------------------------------------------------
    cursor.execute('DELETE FROM Outs WHERE trans = ?',(trans,))


    connection.commit()
    return True

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

