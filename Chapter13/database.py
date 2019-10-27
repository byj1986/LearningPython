import sqlite3

conn = sqlite3.connect('sample.db')
curs = conn.cursor()
# curs.execute("CREATE TABLE IF NOT EXISTS Person(Name char(50), Age INTEGER)")

# curs.execute("INSERT INTO Person(Name, Age) VALUES ('bob', '32')")
# conn.commit()
curs.execute("SELECT Name, Age FROM Person")
for row in curs.fetchall():
    print(row)
# print(res)
# names = [f[0] for f in curs.description]
# print(names)
conn.commit()
conn.close()
