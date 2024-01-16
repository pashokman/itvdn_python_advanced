import sqlite3

conn = sqlite3.connect('db.sqlite3')

conn.execute('CREATE TABLE IF NOT EXISTS "users" (id, first_name, last_name, birthday)')
conn.execute('SELECT * FROM "users"')
conn.execute(
    """INSERT INTO users(id, first_name, last_name, birthday)
       VALUES (1, "Taras", "Shevchenko", "08-10-1815")
    """)

conn.execute(
    """INSERT INTO users(id, first_name, last_name, birthday)
       VALUES (2, "Ivan", "Ogienko", "07-12-1903"),
              (3, "Lesia", "Ukrainka", "15-08-1850")
    """)

users = conn.execute('SELECT * FROM "users"').fetchall()
print(users)
cursor = conn.execute('SELECT * FROM "users";')
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
# cursor.close()

try:
    cursor = conn.execute('SELECT * FROM "tags"')
except sqlite3.OperationalError as e:
    print(e)

first_name = "Ivan"
sql_text = 'SELECT * FROM users WHERE first_name = "%s"' % (first_name)
print(sql_text)
first_name = '"Ivan"'
sql_text = 'SELECT * FROM users WHERE first_name = "%s"' % (first_name)
print(sql_text)

sql_text = 'SELECT * FROM users WHERE id = "%s"' % (10)
print(sql_text)
sql_text2 = 'SELECT * FROM users WHERE id = "%s"' % ('0 or id like "%"')
print(sql_text2)

cursor.execute('SELECT * FROM "users" WHERE id = ?', (10,))
cursor.execute('SELECT * FROM "users" WHERE id = :id', {'id': 10})
cursor.close()