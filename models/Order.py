import mysql.connector
from db.settingup import SettingUp

class Order:
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

    def add(self, fields):
        sql = "insert into orders (Date, Customer_Name, Customer_Phone, Model, Brand, Category, Color, price) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7],))
        self.db.commit()

    def get_product_list(self):
        self.cursor.execute("select name, brand, category, color, Selling_Price_M, quanity from product")
        result = self.cursor.fetchall()
        return result
    
    def check_add_order(self,fields):
        for i in range(len(fields)):
            if fields[i].get() == "":
                return 0
        if fields[1].get().isdigit() == False:
            return 0
        return 1
    
    def get_order_list(self):
        self.cursor.execute("select Date, Customer_Name, Customer_Phone, Model, Brand, Category, Color, quantity, price from orders")
        result = self.cursor.fetchall()
        return result