import mysql.connector

"""
    This class is used to create a product object    
"""

class Product:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tungntl1234",
            database="motorbikemanagement",
            charset="utf8"
        )
        self.cursor = self.db.cursor()


    # add a product to database include name, price, quantity, category
    def add(self, fields):
        response = 0
        try:
            # the name is a foreign key of brand table and category for category table
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Product (
                `ID` INT NOT NULL PRIMARY KEY,
                `Name` VARCHAR(255) CHARACTER SET utf8,
                `Brand` VARCHAR(255) CHARACTER SET utf8,
                `Category` VARCHAR(255) CHARACTER SET utf8,
                FOREIGN KEY (`Brand`) REFERENCES Brand(name),
                FOREIGN KEY (`Category`) REFERENCES Category(name)
            );

            DROP TRIGGER IF EXISTS update_brand_quantity;
            DELIMITER $$
            CREATE TRIGGER update_brand_quantity AFTER INSERT ON Product
            FOR EACH ROW
            BEGIN
                UPDATE Brand
                SET quantity = quantity + 1
                WHERE name = new.Brand;
                
                UPDATE Category
                SET quantity = quantity + 1
                WHERE name = new.Category;
            END $$
            DELIMITER ;
            """)
        except:
            pass
        sql = "insert into product values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get(), fields[4].get(), fields[5].get(), fields[6].get(), fields[7].get(), fields[8].get(), fields[9].get(), fields[10].get(), fields[11].get(), fields[12].get(), fields[13].get(), fields[14].get(), fields[15].get(), fields[16].get(), fields[17].get())
        self.cursor.execute(sql)
        # check if the product is already in database
        self.cursor.execute("select * from product where (Name = %s)", (fields[1].get()))
        result = self.cursor.fetchall()
        if result:
            return response
        else:
            self.cursor.execute(sql)
            self.db.commit()
            response = self.cursor.rowcount
            return response
    
    def getName(self, name):
        query = "SELECT * FROM product WHERE name LIKE %s;"
        self.cursor.execute(query, ('%' + name + '%',))
        self.db.commit()
        result = self.cursor.fetchall()
        return result
    
    def getBrand(self, brand):
        query = "SELECT * FROM product WHERE brand LIKE %s;"
        self.cursor.execute(query, ('%' + brand + '%',))
        self.db.commit()
        result = self.cursor.fetchall()
        return result
    
    def displayBrand(self):
        query = "Drop table if exists brands;"   
        self.cursor.execute(query)
        self.db.commit()
        query = """
            create table if not exists brands (
                select Brand, concat(COUNT(Brand)) as Quantity from product group by Brand
            );
        """

        self.cursor.execute(query)
        self.db.commit()
        query = "select * from brands;"
        self.cursor.execute(query)
        self.db.commit()
        result = self.cursor.fetchall()
        return result
    
    def displayCategory(self):
        query = "Drop table if exists categories;"   
        self.cursor.execute(query)
        self.db.commit()
        query = """
            create table if not exists categories (
                select Category, concat(COUNT(Category)) as Quantity from product group by Category
            );
        """
        self.cursor.execute(query)
        self.db.commit()
        query = "select * from categories;"
        self.cursor.execute(query)
        self.db.commit()
        result = self.cursor.fetchall()
        return result  

    def delete(self, id):
        query = "delete from product where id = %s"
        self.cursor.execute(query, (id,))
        self.db.commit()
        return self.cursor.rowcount 
    
    