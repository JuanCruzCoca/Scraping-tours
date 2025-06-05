import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

new_rows = [('Band A', 'DD', '2088.10.15'), 
            ('Band B', 'eD', '2088.10.15')]

cursor.executemany("INSERT INTO events VALUES (?, ?, ?)", new_rows)
connection.commit()