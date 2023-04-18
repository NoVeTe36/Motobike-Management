import mysql.connector
import re
from datetime import datetime

"""
    This class is used to create a brand object
"""

class User:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tungntl1234",
            database="motorbikemanagement",
            charset="utf8"
        )
        self.cursor = self.db.cursor()
    
    def info(self, username): 
        sql = "SELECT username, fullname, dob, email, address FROM user_data WHERE username = %s"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchone()
        self.db.commit()
        return result
    
    # check valid date of birth (dd/mm/yyyy)
    def validate_dob(self, event, entry):
        regex = r'\b[0-9]{2}\/[0-9]{2}\/[0-9]{4}\b'
        if re.fullmatch(regex, entry.get()):
            return True
        else:
            return False
    
    # check valid email
    def validate_email(self, event, entry):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, entry.get()):
            return True
        else:
            return False

    def edit(self, field, username):
        if not self.validate_email(self, field[2]) or not self.validate_dob(self, field[1]):
            return 0
        else:
            sql = "UPDATE user_data SET fullname = %s, dob = %s, email = %s, address = %s WHERE username = %s"
            self.cursor.execute(sql, (field[0].get(), field[1].get(), field[2].get(), field[3].get(), username,))
            self.db.commit()
            return 1

    def get_login_history(self, username):
        sql = "SELECT DISTINCT DATE(time_login) FROM login_history WHERE username = %s"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchall()        
        self.db.commit()
        # result_list = []
        # for i in range(len(result)):
        #     result_list.append(result[i][0])
        # return result_list
        return result
