import sqlite3
class User:
    def __init__(self, _id,username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(select_query, (username,))
        row = result.fetchone()
        print("Inside find_by_username", row)
        if row is not None:
            user = cls(row[0], row[1], row[2])
            # user = cls(*row) # *row ==> row[0], row[1], row[2]
        else:
            user =None
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(select_query, (_id,))
        row = result.fetchone()
        if row is not None:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row) # *row ==> row[0], row[1], row[2]
        else:
            user =None
        return user