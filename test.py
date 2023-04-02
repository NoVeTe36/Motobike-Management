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
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Brand (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) CHARACTER SET utf8,
                quantity INT DEFAULT 0,
                INDEX brand_idx(name)
            );
            """)
        except:
            pass

    def add(self, name):
        response = 0
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
        return response

    def delete(self, name):
        response = 0
        # check if the brand is already in database
        self.cursor.execute("SELECT * FROM brand WHERE (Name = %s)", (name,))
        result = self.cursor.fetchall()
        if len(result) == 0:
            pass
        else:
            sql = "DELETE FROM brand WHERE (Name = %s)"
            self.cursor.execute(sql, (name,))
            self.db.commit()
            response = self.cursor.rowcount
        return response
    
    def update(self, name, newName):
        response = 0
        # check if the brand is in database or not
        self.cursor.execute("SELECT * FROM brand WHERE (Name = %s)", (name,))
        result = self.cursor.fetchall()
        if len(result) == 0:
            pass
        else:
            sql = "UPDATE brand SET Name = %s WHERE Name = %s"
            self.cursor.execute(sql, (newName, name))
            self.db.commit()
            response = self.cursor.rowcount
        return response       

    def get(self, name):
        self.cursor.execute("SELECT * FROM brand WHERE (Name = %s)", (name,))
        result = self.cursor.fetchall()
        return result

    def get_all(self):
        self.cursor.execute("SELECT * FROM brand")
        result = self.cursor.fetchall()
        columns = [column[0] for column in self.cursor.description]  # get column names
        rows = []
        for row in result:
            row_dict = {}
            for i in range(len(columns)):
                row_dict[columns[i]] = row[i]
            rows.append(row_dict)
        return rows

class Main:
    def __init__(self):
        self.brand = Brand()

    def add(self, name):
        return self.brand.add(name)
    
    def delete(self, name):
        return self.brand.delete(name)
    
    def update(self, name, newName):
        return self.brand.update(name, newName)   

    def get(self, name):
        return self.brand.get(name)

    def get_all(self):
        return self.brand.get_all() 

if __name__ == "_main_":
    num = int(input("Enter number of brand: "))
    for i in range(0, num):
        name = input("Enter brand name: ")
        main = Main()
        main.brand.add(name)
        
    for i in range(0, num):
        name = input("Enter brand name: ")
        main = Main()
        main.delete(name)

    for i in range(0, num):
        name = input("Enter brand name: ")
        newName = input("Enter new brand name: ")
        main = Main()
        main.update(name, newName)

    for i in range(0, num):
        name = input("Enter brand name: ")
        main = Main()
        main.get(name)

    print("All brand: ")
    main = Main()
    allBrand = main.get_all()
    print(allBrand)