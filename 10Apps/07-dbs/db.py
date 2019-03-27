import sqlite3

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")

def insert(item, quantity, price):
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))

def view():
    cur.execute("SELECT * FROM STORE")
    rows = cur.fetchall()
    return rows

conn = sqlite3.connect("lite.db")
cur = conn.cursor()
create_table()
insert("wine_glass", 10, 15)
insert("water_glass", 20, 0.5)
for (d,q,p) in view():
    print("Price: {0} Quantity: {1} Description: {2}".format(q,p,d))

conn.commit()
conn.close()

