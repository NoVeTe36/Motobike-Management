import mysql.connector

class SettingUp:
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
                `id` INT AUTO_INCREMENT PRIMARY KEY,
                `name` VARCHAR(255),
                `quantity` INT DEFAULT 0,
                INDEX brand_idx(name)
            );
            """)
        except:
            pass

        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Category (
                `id` INT AUTO_INCREMENT PRIMARY KEY,
                `name` VARCHAR(255),
                `quantity` INT DEFAULT 0,
                INDEX category_idx(name)
            );
            """)
        except:
            pass

        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS product (
                    `ID` INT primary key auto_increment,
                    `Name` VARCHAR(255) CHARACTER SET utf8,
                    `Brand` VARCHAR(255) CHARACTER SET utf8,
                    `Category` VARCHAR(255) CHARACTER SET utf8,
                    `Length_mm` NUMERIC(25, 2),
                    `Width_mm` NUMERIC(25, 2),
                    `Height_mm` NUMERIC(25, 2),
                    `Mass_kg` NUMERIC(25, 2),
                    `Fuel_Capacity_l` NUMERIC(25, 3),
                    `Fuel_Consumption_l_100km` NUMERIC(25, 3),
                    `Engine_Type` VARCHAR(255) CHARACTER SET utf8,
                    `Maximize_Efficiency_kW_minute` NUMERIC(25, 3),
                    `Color` VARCHAR(25) CHARACTER SET utf8,
                    `Selling_Price_M` NUMERIC(25, 3),
                    `quanity` INT
                );

                """)            
        except:
            pass


        try:
            self.cursor.execute("""
                DROP TRIGGER IF EXISTS update_brand_quantity;
                DELIMITER $$
                CREATE TRIGGER update_brand_quantity AFTER INSERT ON product
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
