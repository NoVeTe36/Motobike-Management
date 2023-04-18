import tkinter as tk
from tkinter import ttk
from views.gifthreading import *
from views.Trivial import *

class ManageOrdersView:
    def __init__(self, contentFrame, controller, user, root):
        self.homeController = controller
        self.window = root
        self.user = user
        self.contentFrame = contentFrame
        self.user_info = self.homeController.take_info(self.user)
    
    def displayManageOrders(self):
        contentFrame = self.contentFrame
        clearFrame(contentFrame)
        tk.Label(contentFrame, text="Orders history",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        tk.Frame(contentFrame, width=10, height=24, bg='#cc0000').place(x=48, y=70)

        orderFrame = tk.Frame(contentFrame, bg = "#cccccc")
        orderFrame.place(x=20, y=160, width=970, height=440)

        searchBar = ttk.Entry(contentFrame, font = ('Helvetica', 10))
        searchBar.place(x=780, y=125, width=210, height=25)

        # Treeview

        self.tree = self.homeController.showTreeView_OrderList(contentFrame, orderFrame,searchBar.get())
        def searchByName(e):
            self.tree = self.homeController.showTreeView_OrderList(contentFrame, orderFrame, searchBar.get())
            return self.tree
        searchBar.bind('<KeyRelease>', searchByName)