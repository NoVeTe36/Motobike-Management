import mysql.connector
from db.settingup import SettingUp

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
        SettingUp()

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

            brand_sql = "UPDATE Brand SET quantity = quantity + 1 WHERE (Name = %s)"
            self.cursor.execute(brand_sql, (fields[1].get(),))
            self.db.commit()

            category_sql = "UPDATE Category SET quantity = quantity + 1 WHERE (Name = %s)"
            self.cursor.execute(category_sql, (fields[2].get(),))
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
    
    def getName(self, name):
        query = "SELECT name, brand, category, length_mm, width_mm, height_mm, mass_kg, fuel_capacity_l, fuel_consumption_l_100km, engine_type, Maximize_Efficiency_kW_minute, color, Selling_Price_M, quanity FROM product WHERE name LIKE %s;"
        self.cursor.execute(query, ('%' + name + '%',))
        result = self.cursor.fetchall()
        self.db.commit()
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
        for field in fields:
            if field.get() == "":
                return 0
        self.cursor.execute("select * from product where (Name = %s)", (fields[0].get(),))
        result = self.cursor.fetchall()
        if result:
            return -1
        return 1
    
    def get_product_list(self):
        self.cursor.execute("select name, brand, category, length_mm, width_mm, height_mm, mass_kg, fuel_capacity_l, fuel_consumption_l_100km, engine_type, Maximize_Efficiency_kW_minute, color, Selling_Price_M, quanity from product")
        result = self.cursor.fetchall()
        self.db.commit()
        return result
    
    def delete_product(self, name):
        self.cursor.execute("select brand, category from product where (Name = %s)", (name,))
        result = self.cursor.fetchall()
        brand = result[0][0]
        category = result[0][1]
        print(brand, category)

        brand_sql = "UPDATE Brand SET quantity = quantity - 1 WHERE (Name = %s)"
        self.cursor.execute(brand_sql, (brand,))
        self.db.commit()

        category_sql = "UPDATE Category SET quantity = quantity - 1 WHERE (Name = %s)"
        self.cursor.execute(category_sql, (category,))
        self.db.commit()

        self.cursor.execute("delete from product where name = %s", (name,))
        self.db.commit()

    def update_product(self, fields):
        response = 0
        for field in fields:
            if field.get() == "":
                return response

        # check if the product is already in database
        self.cursor.execute("SELECT * FROM product WHERE Name = %s", (fields[0].get(),))
        result = self.cursor.fetchall()
        if not result:
            return response

        # update product if it exists
        # check for other products except the one being updated
        self.cursor.execute("SELECT * FROM product WHERE Name != %s", (fields[0].get(),))
        result = self.cursor.fetchall()
        for row in result:
            # update brand and category quantities
            self.cursor.execute("""
                UPDATE Brand
                SET quantity = quantity - %s
                WHERE name = %s;
                
                UPDATE Category
                SET quantity = quantity - %s
                WHERE name = %s;
            """, (row[14], row[2], row[14], row[3]))
            
        # update product information
        sql = """
            UPDATE product
            SET name = %s, brand = %s, category = %s, length_mm = %s, width_mm = %s, height_mm = %s,
                mass_kg = %s, fuel_capacity_l = %s, fuel_consumption_l_100km = %s, engine_type = %s,
                Maximize_Efficiency_kW_minute = %s, color = %s, Selling_Price_M = %s, quanity = %s
            WHERE Name = %s
        """
        self.cursor.execute(sql, (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get(),
                                fields[4].get(), fields[5].get(), fields[6].get(), fields[7].get(),
                                fields[8].get(), fields[9].get(), fields[10].get(), fields[11].get(),
                                fields[12].get(), fields[13].get(), fields[0].get()))
        self.db.commit()

        # update brand and category quantities for the updated product
        self.cursor.execute("""
            UPDATE Brand
            SET quantity = quantity + %s
            WHERE name = %s;
            
            UPDATE Category
            SET quantity = quantity + %s
            WHERE name = %s;
        """, (fields[13].get(), fields[1].get(), fields[13].get(), fields[2].get()))

        response = self.cursor.rowcount
        return response  

    
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


    