import mysql.connector

"""
    This class is used to create a brand object
"""

class Brand:
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
            CREATE TABLE IF NOT EXISTS Brand (
                `id` INT AUTO_INCREMENT PRIMARY KEY,
                `name` VARCHAR(255) CHARACTER SET utf8,
                `quantity` INT DEFAULT 0,
                INDEX brand_idx(name)
            );
            """)
        except:
            pass
        sql = "insert into brand (Name) values (%s)", (name)
        self.cursor.execute(sql)
        # check if the brand is already in database
        self.cursor.execute("select * from brand where (Name = %s)", (name))
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
        sql = "delete from brand where (Name = %s)", (name)
        self.cursor.execute(sql)
        # check if the brand is already in database
        self.cursor.execute("select * from brand where (Name = %s)", (name))
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
        sql = "update brand set Name = %s where Name = %s", (newName, name)
        self.cursor.execute(sql)
        # check if the brand is already in database
        self.cursor.execute("select * from brand where (Name = %s)", (name))
        result = self.cursor.fetchall()
        if result:
            return response
        else:
            self.cursor.execute(sql)
            self.db.commit()
            response = self.cursor.rowcount
            return response