import mysql.connector
from tkinter import messagebox

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
        # check if the brand is already in database
        self.cursor.execute("SELECT * FROM brand WHERE (Name = %s)", (name,))
        result = self.cursor.fetchall()
        if len(result) > 0:
            print("Error: Brand already exists")
            pass
        else:
            sql = "INSERT INTO Brand (Name) VALUES (%s)"
            self.cursor.execute(sql, (name,))
            self.db.commit()
            response = self.cursor.rowcount
            print("Response to add "+ str(response))
        print("Response to add "+ str(response))
        return response
        

class Main:
    def __init__(self):
        self.brand = Brand()

    def add(self, name):
        return self.brand.add(name)
    

if __name__ == "__main__":
    num = int(input("Enter number of brand: "))
    for i in range(0, num):
        name = input("Enter brand name: ")
        main = Main()
        main.add(name)
