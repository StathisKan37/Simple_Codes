# Exercise:
# ---------------------------------------------------------------------
# Whrite an SQL query to return all the products of the database in
# three columns: Product name, price per unit and new price
# (new price = price per unit * 1.1)

import sqlite3
# Connecting to 'test_database.db' database
database_1 = sqlite3.connect('test_database.db')
# Creating a cursor
cursor = database_1.cursor()

# Optionally droping each table in 'test_database.db'
cursor.execute("DROP TABLE IF EXISTS table_1")

# Creating a table
cursor.execute("CREATE TABLE table_1(product text, unit_price numeric)")
# Inserting new values in table_1
cursor.execute("""
INSERT INTO table_1 (product,unit_price) VALUES
	('Jameson', 20.72),
	('Jameson Black', 34.20),
	('Johnie Walker Red', 16.90),
	('Johnie Walker Black', 27.58),
	('Famous Grouse', 18.10),
	('Grants', 18.92)
""")

# Querying the products, the price and the new price
cursor.execute("SELECT product, unit_price AS original_price, unit_price * 1.1 AS new_price FROM table_1")
for product, price, new_price in cursor.fetchall():
    print(f'{product:<22}  {price:>6.2f}  {new_price:>6.2f}')

# Commiting all the changes
database_1.commit()
# Closing the connection
database_1.close()
