import sqlite3

conn = sqlite3.connect('clash_royale.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT * from cards_table order by Type;
''')

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
