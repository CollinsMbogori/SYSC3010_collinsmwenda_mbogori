import sqlite3 

conn = sqlite3.connect("demo.db")
conn.row_factory = sqlite3.Row;
curs = conn.cursor()

curs.execute('''CREATE TABLE IF NOT EXISTS sensors (sensorID integer, type TEXT, zone TEXT)''');
curs.execute('''INSERT into sensors values (1, "door","kitchen")''');
curs.execute('''INSERT into sensors values (2, "temperature","kitchen")''');
curs.execute('''INSERT into sensors values (3, "door","garage")''');
curs.execute('''INSERT into sensors values (4, "motion","garage")''');
curs.execute('''INSERT into sensors values (5, "temperature","garage")''');

conn.commit();
#Create Tables
#curs.executescript(sensors)
#Read Table Schema into a Variable and remove all New Line Chars
curs.execute('SELECT * FROM sensors WHERE zone = "kitchen" AND type = "door" ');
for row in curs:
    print(row['sensorID'],row['type'],row['zone'] );
    
conn.close();