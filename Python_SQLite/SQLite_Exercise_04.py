# Excercise:
# ---------------------------------------------------------------------
# Write a query and join the names with the cars

import sqlite3

# Connecting to 'test_database.db' database
database_1 = sqlite3.connect('test_database.db')
# Creating a cursor
cursor = database_1.cursor()

# Optionally droping each table in 'test_database.db'
cursor.execute("DROP TABLE IF EXISTS table_1")
cursor.execute("DROP TABLE IF EXISTS table_2")
cursor.execute("DROP TABLE IF EXISTS table_3")

# Table with names
cursor.execute("CREATE TABLE table_1(name text, last_name text)")
cursor.execute("""
INSERT INTO table_1 (name, last_name) VALUES
	('Alice','Johnson'),
	('Bob','Martinez'),
	('Charlie','Nguyen'),
	('Diana','Smith'),
	('Ethan','Brown')
""")

# Table with cars
cursor.execute("CREATE TABLE table_2(owner_id integer, brand text, model text)")
cursor.execute("""
INSERT INTO table_2 (owner_id, brand, model) VALUES
	(4, 'Honda', 'Civic'),
	(3, 'Toyota', 'Corolla'),
	(1, 'Ford', 'Mustang'),
	(5, 'Audi', 'A4'),
	(2, 'Mazda', 'CX-5')
""")

# Querying the names and the cars
cursor.execute("SELECT * FROM table_1 JOIN table_2 ON table_2.owner_id = table_1.rowid")
for i in cursor.fetchall():
    print(f'{i[0]} {i[1]} - {i[3]} {i[4]}')


# Commiting all the changes
database_1.commit()
# Closing the connection
database_1.close()
