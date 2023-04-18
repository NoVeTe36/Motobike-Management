import tkinter as tk
from tkinter import messagebox
from views.gifthreading import *
from views.Trivial import *

class UserView:
    def __init__(self, contentFrame, controller, user, root):
        self.homeController = controller
        self.window = root
        self.user = user
        self.contentFrame = contentFrame
        self.user_info = self.homeController.take_info(self.user)
    
    def displayUser(self):
        contentFrame = self.contentFrame
        clearFrame(contentFrame)
        tk.Label(contentFrame, text = "User Information", font = ('Helvetica', 25, 'bold'), bg = '#fff').place(x = 60, y = 60)

        usernameLabel = tk.Label(contentFrame, text = 'Username:', bg = '#fff', font = ('Helvetica', 16))
        usernameLabel.place(x = 110, y = 160)
        usernameField = tk.Label(contentFrame, text = self.user_info[0], bg = '#fff', fg = "#000000", font = ('Helvetica', 16), anchor = 'w')
        usernameField.place(x = 300, y = 160, width = 400)

        fullnameLabel = tk.Label(contentFrame, text = 'Fullname:', bg = '#fff', font = ('Helvetica', 16))
        fullnameLabel.place(x = 110, y = 200)
        fullnameField = tk.Label(contentFrame, text = self.user_info[1], bg = '#fff', fg = "#000000", font = ('Helvetica', 16), anchor = 'w')
        fullnameField.place(x = 300, y = 200, width = 400)

        DOBLabel = tk.Label(contentFrame, text = 'Date of Birth:', bg = '#fff', font = ('Helvetica', 16))
        DOBLabel.place(x = 110, y = 240)
        DOBField = tk.Label(contentFrame, text = self.user_info[2], bg = '#fff', fg = "#000000", font = ('Helvetica', 16), anchor = 'w')
        DOBField.place(x = 300, y = 240, width = 400)

        emailLabel = tk.Label(contentFrame, text = 'Email:', bg = '#fff', font = ('Helvetica', 16))
        emailLabel.place(x = 110, y = 280)
        emailField = tk.Label(contentFrame, text = self.user_info[3], bg = '#fff', fg = "#000000", font = ('Helvetica', 16), anchor = 'w')
        emailField.place(x = 300, y = 280, width = 400)

        addressLabel = tk.Label(contentFrame, text = 'Address:', bg = '#fff', font = ('Helvetica', 16))
        addressLabel.place(x = 110, y = 320)
        addressField = tk.Label(contentFrame, text = self.user_info[4], bg = '#fff', fg = "#000000", font = ('Helvetica', 16), anchor = 'w')
        addressField.place(x = 300, y = 320, width = 400)

        editBtn = HoverButton(contentFrame, text = 'Edit', bg = '#238636', fg = '#fff', font = ('Helvetica', 10, 'bold'), activebackground = '#238636', activeforeground = '#fff', relief = 'flat', command = lambda: [editFunction(contentFrame), editBtn.destroy()], cursor = 'hand2')
        editBtn.place(x = 610, y = 360, width = 90)

        # self.calendar(contentFrame, self.user)

        def editFunction(contentFrame):
            Fields = []
            fullNameEntry = tk.Entry(contentFrame, bg = "#ffffff", fg = "#000000", font = ('Helvetica', 16))
            fullNameEntry.insert(0, self.user_info[1])
            fullNameEntry.place(x = 300, y = 200, width = 400)
            Fields.append(fullNameEntry)

            DOBEntry = tk.Entry(contentFrame, bg = "#ffffff", fg = "#000000", font = ('Helvetica', 16))
            DOBEntry.insert(0, self.user_info[2])
            DOBEntry.place(x = 300, y = 240, width = 400)
            Fields.append(DOBEntry)

            emailEntry = tk.Entry(contentFrame, bg = "#ffffff", fg = "#000000", font = ('Helvetica', 16))
            emailEntry.insert(0, self.user_info[3])
            emailEntry.place(x = 300, y = 280, width = 400)
            Fields.append(emailEntry)

            addressEntry = tk.Entry(contentFrame, bg = "#ffffff", fg = "#000000", font = ('Helvetica', 16))
            addressEntry.insert(0, self.user_info[4])
            addressEntry.place(x = 300, y = 320, width = 400)
            Fields.append(addressEntry)

            confirmBtn = HoverButton(contentFrame, text = 'Confirm', bg = '#238636', fg = '#fff', font = ('Helvetica', 10, 'bold'), width=10, activebackground = '#238636', activeforeground = '#fff', relief = 'flat', command = lambda: self.confirming(Fields, self.user), cursor = 'hand2')
            confirmBtn.place(x = 610, y = 360, width = 90)

            cancelBtn = HoverButton(contentFrame, text = 'Cancel', bg = '#cc0000', fg = '#fff', font = ('Helvetica', 10, 'bold'), width=10, activebackground = '#cc0000', activeforeground = '#fff', relief = 'flat', command = lambda: self.displayUser(contentFrame), cursor = 'hand2')
            cancelBtn.place(x = 505, y = 360, width = 90)

    def confirming(self, Fields, username):
        self.homeController.edit_info(Fields, username)
        if self.homeController.edit_info(Fields, username) == 1:
            messagebox.showinfo("Success", "Edit successfully")
            self.user_info = self.homeController.take_info(self.user)
            self.displayUser()
        else:
            messagebox.showinfo("Error", "Edit failed")