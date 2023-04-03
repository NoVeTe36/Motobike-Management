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
        sql = "insert into product (Date, Customer_Name, Customer_Phone, Model, Brand, Category, ) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get(), fields[4].get(), fields[5].get(), fields[6].get(), fields[7].get(),))
        self.cursor.fetchall()
        self.db.commit()