import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)

    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS(NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, "
                 "RATING TEXT)")

    print("Table created successfully")
    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)

    conn.execute("INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES (?, ?, ?, ?, ?)")

    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn = sqlite3.connect(dbname)

    cur = conn.cursor()

    cur.execute("SELECT * FROM OYO_HOTELS")

    table_data = cur.fetchall()
    for record in table_data:
        print(record)
