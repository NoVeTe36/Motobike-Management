import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import time, datetime
from views.View import View
from db.settingup import SettingUp
from views.gifthreading import *
from views.Trivial import *

class DashboardView:
    def __init__(self, contentFrame, controller, user, root):
        self.homeController = controller
        self.window = root
        self.user = user
        self.contentFrame = contentFrame
        self.user_info = self.homeController.take_info(self.user)
        
    def displayDashboard(self):
        contentFrame = self.contentFrame
        clearFrame(contentFrame)
        tk.Label(contentFrame, text="Dashboard",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        tk.Frame(contentFrame, width=10, height=24, bg='#cc0000').place(x=48, y=70)
        contentFrameOne = tk.Frame(contentFrame, width=440, height=202, bg='#cb2027')
        contentFrameOne.place(x=60, y=170)
        tk.Label(contentFrameOne, text = "Total Product", font =("Helvetica", 20, 'bold'), bg = '#cb2027', fg='#ffffff').place(x = 200, y = 40)
        tk.Label(contentFrameOne, text = self.homeController.get_sum_product(), font =("Helvetica", 30, 'bold'), bg = '#cb2027', fg='#ffffff').place(x = 260, y = 90)
        self.productGif = GifContent(self.window, contentFrameOne, 2, '../img/product_1.gif', 10, 55, "#cb2027")
        self.productGif.run()

        contentFrameTwo = tk.Frame(contentFrame, width=440, height=202, bg='#179648')
        contentFrameTwo.place(x=515, y=170)
        tk.Label(contentFrameTwo, text = "Revenue", font =("Helvetica", 20, 'bold'), bg = '#179648', fg='#ffffff').place(x = 222, y = 40)
        tk.Label(contentFrameTwo, text = self.homeController.get_profit(), font =("Helvetica", 30, 'bold'), bg = '#179648', fg='#ffffff').place(x = 210, y = 90)
        self.revenueGif = GifContent(self.window, contentFrameTwo, 2, '../img/revenue_3.gif', 10, 45, "#179648")
        self.revenueGif.run()

        contentFrameThree = tk.Frame(contentFrame, width=440, height=202, bg='#263981')
        contentFrameThree.place(x=60, y=400)
        tk.Label(contentFrameThree, text = "Brands", font =("Helvetica", 20, 'bold'), bg = '#263981', fg='#ffffff').place(x = 250, y = 40)
        tk.Label(contentFrameThree, text = self.homeController.get_sum_brand(), font =("Helvetica", 30, 'bold'),bg='#263981', fg = '#ffffff').place(x = 280, y = 90)
        self.brandGif = GifContent(self.window, contentFrameThree, 2, '../img/brands_2.gif', 10, 45, "#263981")
        self.brandGif.run()

        contentFrameFour = tk.Frame(contentFrame, width=440, height=202, bg='#f58217')
        contentFrameFour.place(x=515, y=400)
        tk.Label(contentFrameFour, text = "Sold Product", font =("Helvetica", 20, 'bold'), bg = '#f58217', fg='#ffffff').place(x = 200, y = 40)
        tk.Label(contentFrameFour, text = self.homeController.get_sum_soldproduct(), font =("Helvetica", 30, 'bold'), bg = '#f58217', fg='#ffffff').place(x = 270, y = 90)
        self.soldProductGif = GifContent(self.window, contentFrameFour, 2, '../img/sold_4.gif', 10, 55, "#f58217")
        self.soldProductGif.run()