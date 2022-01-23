import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Createing table
create_table_query = """ CREATE TABLE users (
    id int,
    username text, 
    password
) """

cursor.execute(create_table_query)

# Insert users 
user_list = [(1, 'bibek', 'passwd'),
(2, 'ajay', 'passwd'),]

insert_query = " INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query, user_list)

select_query = "SELECT * FROM users WHERE username=?"
result = cursor.execute(select_query, ('bibek',))
row = result.fetchone()
print("Inside find_by_username", row)
# if row is not None:
#     print(row)

connection.commit()
connection.close()
