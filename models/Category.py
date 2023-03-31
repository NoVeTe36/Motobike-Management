import mysql.connector

"""
    This class is used to create a category object
"""

class Category:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tungntl1234",
            database="motorbikemanagement",
            charset="utf8"
        )
        self.cursor = self.db.cursor()

    def add(self, name):
        response = 0
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Category(
                `id` int AUTO_INCREMENT PRIMARY KEY,
                `name` VARCHAR(255) CHARACTER SET utf8,
                `quantity` INT DEFAULT 0,
                INDEX cate_idx(name)
            );
            """)
        except:
            pass
        sql = "insert into category (Name) values (%s)", (name)
        self.cursor.execute(sql, (name))
        # check if the category is already in database
        self.cursor.execute("select * from category where (Name = %s)", (name))
        result = self.cursor.fetchall()
        if result:
            return response
        else:
            self.cursor.execute(sql)
            self.db.commit()
            response = self.cursor.rowcount
            return response
        
    def delete(self, name):
        response = 0
        sql = "delete from category where (Name = %s)", (name)
        self.cursor.execute(sql)
        # check if the category is already in database
        self.cursor.execute("select * from category where (Name = %s)", (name))
        result = self.cursor.fetchall()
        if result:
            return response
        else:
            self.cursor.execute(sql)
            self.db.commit()
            response = self.cursor.rowcount
            return response
        
    def update(self, name, newName):
        response = 0
        sql = "update category set Name = %s where Name = %s", (newName, name)
        # check if the category is in database or not
        self.cursor.execute("select * from category where (Name = %s)", (name))
        result = self.cursor.fetchall()
        if result:
            return response
        else:
            self.cursor.execute(sql)
            self.db.commit()
            response = self.cursor.rowcount
            return response