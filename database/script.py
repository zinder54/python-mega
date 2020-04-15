import psycopg2

def CreatTable():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432'")
                      #^^^^connects to database created in postgres
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #^^^ creates table of data in database sql commands always in ""
    conn.commit() #creates connection to #db
    conn.close() # closes connection to db

def insert(item, quantity, price): ##creates function to insert data into table, stops duplicate data
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432'")
                 #^^connects to database created in postgres
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    ## ^^('%s','%s','%s')" % (item,quantity,price)) <<one way to do the above but is susceptable to SQL injections.
    ##^ executes sql command, "if use double speech marks'use single within them for string' "
    conn.commit() #creates connection to #db
    conn.close() # closes connection to db

def view(): ##creates a function to view the list in db
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432'") #connects to the # DEBUG:
    cur=conn.cursor()
    cur.execute("SELECT * FROM store") ##selects all info from the db
    rows=cur.fetchall()#fetches the information from the db
    conn.close()#closes connect no need for commit
    return rows

def delete(item): #creates function to delete duplicates
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,)) #deletes duplicates passes item through function parameter
    conn.commit()
    conn.close()

def update(quantity, price, item): #creates function to update sql DB
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item)) #updates tabel only were the
    conn.commit() #                                   ^^ item is called in a parameter. if no item then it does not update
    conn.close()

CreatTable()
update(11,6,"Orange")#calls the function above and passes the parameters to be updated in ()
#delete("Apple")
#insert("Apple", 15,16) #inserts data into db table
print(view()) #prints the view function
