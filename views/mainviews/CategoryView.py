import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import time, datetime
from views.View import View
from db.settingup import SettingUp
from views.gifthreading import *
from views.Trivial import *
from views.mainviews.ManageProductsView import ManageProductsView

class CategoryView:
    def __init__(self, contentFrame, controller, user, root):
        self.homeController = controller
        self.window = root
        self.user = user
        self.contentFrame = contentFrame
        self.user_info = self.homeController.take_info(self.user)

    def displayCategory(self):
        contentFrame = self.contentFrame
        clearFrame(contentFrame)
        tk.Label(contentFrame, text="Category",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        tk.Frame(contentFrame, width=10, height=24, bg='#cc0000').place(x=48, y=70)
        # Manual Motorcycle Box
        def directToManual(e):
            ManageProductsView(self.contentFrame, self.homeController, self.user, self.window).displayManageProductsByCategory("manual")
        self.manualImg = Image.open("./img/manual.png")
        self.manualResizeImg = self.manualImg.resize((200, 200))
        self.manualResizeImg = ImageTk.PhotoImage(self.manualResizeImg)
        self.manual = tk.Label(contentFrame, image=self.manualResizeImg, bg='#ffffff', cursor='hand2')
        self.manual.place(x=180, y=140)
        self.manual.bind('<Button-1>', directToManual)

        # Scooter Box
        def directToScooter(e):
            ManageProductsView(self.contentFrame, self.homeController, self.user, self.window).displayManageProductsByCategory("scooter")
        self.scooterImg = Image.open("./img/scooter.png")
        self.scooterImg = self.scooterImg.resize((200, 200))
        self.scooterImg = ImageTk.PhotoImage(self.scooterImg)
        self.scooter = tk.Label(contentFrame, image=self.scooterImg, bg='#ffffff', cursor='hand2')
        self.scooter.place(x=580, y=140)
        self.scooter.bind('<Button-1>', directToScooter)

        # Sport Box
        def directToSport(e):
            ManageProductsView(self.contentFrame, self.homeController, self.user, self.window).displayManageProductsByCategory("sport")
        self.sportImg = Image.open("./img/sport.png")
        self.sportImg = self.sportImg.resize((200, 200))
        self.sportImg = ImageTk.PhotoImage(self.sportImg)
        self.sport = tk.Label(contentFrame, image=self.sportImg, bg='#ffffff', cursor='hand2')
        self.sport.place(x=380, y=390)
        self.sport.bind('<Button-1>', directToSport)