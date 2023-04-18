import tkinter as tk
from tkinter import ttk
from views.gifthreading import *
from views.Trivial import *

class BrandView:
    def __init__(self, contentFrame, controller, user, root):
        self.homeController = controller
        self.window = root
        self.user = user
        self.contentFrame = contentFrame
        self.user_info = self.homeController.take_info(self.user)
    
    def displayBrand(self):
        contentFrame = self.contentFrame
        clearFrame(contentFrame)
        # Label "Brand"
        tk.Label(contentFrame, text="Brand",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        tk.Frame(contentFrame, width=10, height=24, bg='#cc0000').place(x=48, y=70)
        # Add new brand
        brandAddEntryBox = ttk.Entry(contentFrame, font = ('Helvetica', 10))
        brandAddEntryBox.place(x = 680, y = 125, width = 235, height = 25)

        saveChangeBtn = HoverButton(contentFrame, text = "Add", bg = '#238686', fg = "#fff", font = ('Helvetica', 10, 'bold'), activebackground = '#238636', activeforeground = '#fff', relief = 'flat', command = lambda: self.homeController.btnAdd_Brand(brandAddEntryBox, tree, contentFrame))
        saveChangeBtn.place(x = 915, y = 125, width = 65, height = 25)

        # Treeview
        tree = self.homeController.showTreeView_BrandList(contentFrame)
        return tree
