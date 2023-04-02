import mysql.connector

class Order:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tungntl1234",
            database="motorbikemanagement",
            charset="utf8"
        )

        try:
            """
            CREATE TABLE IF NOT EXISTS `order` (
                `ID` INT primary key auto_increment,
                `Date` DATE,
                `Customer_Name` VARCHAR(255) CHARACTER SET utf8,
                `Customer_Phone` VARCHAR(255) CHARACTER SET utf8,
                `Model` VARCHAR(255) CHARACTER SET utf8,
                `Brand` VARCHAR(255) CHARACTER SET utf8,
                `Category` VARCHAR(255) CHARACTER SET utf8,
                `Color` VARCHAR(255) CHARACTER SET utf8,
                `Quantity` INT,
                `Total_Price` NUMERIC(18, 3)
            );
            DROP TRIGGER IF EXISTS decrease_quantity;
                DELIMITER $$
                CREATE TRIGGER decrease_quantity AFTER INSERT ON order
                FOR EACH ROW
                BEGIN
                    UPDATE Product
                    SET quanity = quanity - new.Quantity
                    WHERE name = new.Model;
                    
                    UPDATE Brand
                    SET quantity = quantity - new.Quantity
                    WHERE name = new.Brand;

                    UPDATE Category
                    SET quantity = quantity - new.Quantity
                    WHERE name = new.Category;                    
                END $$
                DELIMITER ;
            """
        except:
            pass

        self.cursor = self.db.cursor()

    def add(self, fields):
        sql = "insert into product (Date, Customer_Name, Customer_Phone, Model, Brand, Category, ) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get(), fields[4].get(), fields[5].get(), fields[6].get(), fields[7].get(),))
        self.cursor.fetchall()
        self.db.commit()