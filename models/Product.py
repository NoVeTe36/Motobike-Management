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
        
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS product (
                    `ID` INT primary key auto_increment,
                    `Name` VARCHAR(255) CHARACTER SET utf8,
                    `Brand` VARCHAR(255) CHARACTER SET utf8,
                    `Category` VARCHAR(255) CHARACTER SET utf8,
                    `Length_mm` NUMERIC(9, 2),
                    `Width_mm` NUMERIC(9, 2),
                    `Height_mm` NUMERIC(9, 2),
                    `Mass_kg` NUMERIC(9, 2),
                    `Fuel_Capacity_l` NUMERIC(9, 3),
                    `Fuel_Consumption_l_100km` NUMERIC(9, 3),
                    `Engine_Type` VARCHAR(255) CHARACTER SET utf8,
                    `Maximize_Efficiency_kW_minute` NUMERIC(9, 3),
                    `Color` VARCHAR(25) CHARACTER SET utf8,
                    `Selling_Price_M` NUMERIC(18, 3),
                    `quanity` INT
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
        self.cursor = self.db.cursor()


    # add a product to database include name, price, quantity, category
    def add(self, fields):
        response = 0
        for field in fields:
            if field.get() == "":
                return response
        # check if the product is already in database
        self.cursor.execute("select * from product where (Name = %s)", (fields[0].get(),))
        result = self.cursor.fetchall()
        if result:
            pass
        else:
            sql = "insert into product (name, brand, category, length_mm, width_mm, height_mm, mass_kg, fuel_capacity_l, fuel_consumption_l_100km, engine_type, Maximize_Efficiency_kW_minute, color, Selling_Price_M, quanity) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get(), fields[4].get(), fields[5].get(), fields[6].get(), fields[7].get(), fields[8].get(), fields[9].get(), fields[10].get(), fields[11].get(), fields[12].get(), fields[13].get(),))
            self.db.commit()
            response = self.cursor.rowcount
        return response
    
    def delete(self, name):
        response = 0
        # check if the brand is already in database
        self.cursor.execute("SELECT * FROM product WHERE (Name = %s)", (name,))
        result = self.cursor.fetchall()
        if len(result) == 0:
            pass
        else:
            sql = "DELETE FROM product WHERE (Name = %s)"
            self.cursor.execute(sql, (name,))
            self.db.commit()
            response = self.cursor.rowcount
        return response

    def update(self, oldname, fields):
        response = 0
        # check if the product is already in database
        self.cursor.execute("select * from product where (Name = %s)", (fields[0].get()))
        result = self.cursor.fetchall()
        if result:
            pass
        else:
            sql = "UPDATE product SET Name = %s, Brand = %s, Category = %s, Length_mm = %s, Width_mm = %s, Height_mm = %s, Mass_kg = %s, Fuel_Capacity_l = %s, Fuel_Consumption_l_100km = %s, Engine_Type = %s, Maximize_Efficiency_kW_minute = %s, Color = %s, Selling_Price_M = %s, quanity = %s WHERE (Name = %s)"
            self.cursor.execute(sql, (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get(), fields[4].get(), fields[5].get(), fields[6].get(), fields[7].get(), fields[8].get(), fields[9].get(), fields[10].get(), fields[11].get(), fields[12].get(), fields[13].get(), oldname,))
            self.db.commit()
            response = self.cursor.rowcount
        return response      
    
    def getName(self, name):
        query = "SELECT * FROM product WHERE name LIKE %s;"
        self.cursor.execute(query, ('%' + name + '%',))
        self.db.commit()
        result = self.cursor.fetchall()
        return result
    
    def get_brand_list(self):
        self.cursor.execute("select name from product")
        result = self.cursor.fetchall()
        return result
    
    def get_sum_product(self):
        self.cursor.execute("select sum(quanity) from product")
        result = self.cursor.fetchall()
        result = result[0][0]
        return result
    
    def check_add_product(self,fields):
        for i in range(len(fields)):
            if fields[i].get() == "":
                return 0
        return 1
    
    def get_product_list(self):
        self.cursor.execute("select name, brand, category, length_mm, width_mm, height_mm, mass_kg, fuel_capacity_l, fuel_consumption_l_100km, engine_type, Maximize_Efficiency_kW_minute, color, Selling_Price_M, quanity from product")
        result = self.cursor.fetchall()
        self.db.commit()
        print(result)
        return result
    
    def sort(self, index):
        query = "select name, brand, category, length_mm, width_mm, height_mm, mass_kg, fuel_capacity_l, fuel_consumption_l_100km, engine_type, Maximize_Efficiency_kW_minute, color, Selling_Price_M, quanity from product order by " + index + ";"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    def filter(self, index):
        query = "select name, brand, category, length_mm, width_mm, height_mm, mass_kg, fuel_capacity_l, fuel_consumption_l_100km, engine_type, Maximize_Efficiency_kW_minute, color, Selling_Price_M, quanity from product  order by " + index + ";"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


    