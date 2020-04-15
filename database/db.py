import sqlite3

def CreatTable():
    conn = sqlite3.connect("lite.db") # either creates a new database or connects to existing
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #^^^ creates table of data in database sql commands always in ""
    conn.commit() #creates connection to #db
    conn.close() # closes connection to db

def insert(item, quantity, price): ##creates function to insert data into table, stops duplicate data
    conn = sqlite3.connect("lite.db") # either creates a new database or connects to existing
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))##makes safer from hackers
    ##^ executes sql command, "if use double speech marks'use single within them for string' "
    conn.commit() #creates connection to #db
    conn.close() # closes connection to db

def view(): ##creates a function to view the list in db
    conn=sqlite3.connect("lite.db") #connects to the # DEBUG:
    cur=conn.cursor()
    cur.execute("SELECT * FROM store") ##selects all info from the db
    rows=cur.fetchall()#fetches the information from the db
    conn.close()#closes connect no need for commit
    return rows

def delete(item): #creates function to delete duplicates
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,)) #deletes duplicates passes item through function parameter
    conn.commit()
    conn.close()

def update(quantity, price, item): #creates function to update sql DB
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item)) #updates tabel only were the
    conn.commit() #                                   ^^ item is called in a parameter. if no item then it does not update
    conn.close()

#update(11,5,"Water glass")#calls the function above and passes the parameters to be updated in ()
#delete("Wine Glass")
#insert("Tea Cup", 10,5) #inserts data into db table
print(view()) #prints the view function
