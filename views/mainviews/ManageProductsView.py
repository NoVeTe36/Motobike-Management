import tkinter as tk
from tkinter import ttk
from views.gifthreading import *
from views.Trivial import *

class ManageProductsView:
    def __init__(self, contentFrame, controller, user, root):
        self.homeController = controller
        self.window = root
        self.user = user
        self.contentFrame = contentFrame
        self.user_info = self.homeController.take_info(self.user)

    def displayManageProducts(self):
        contentFrame = self.contentFrame
        try:
            self.tree.destroy()
        except:
            pass
        clearFrame(contentFrame)
        tk.Label(contentFrame, text="Manage products",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        tk.Frame(contentFrame, width=10, height=24, bg='#cc0000').place(x=48, y=70)

        self.productFrame = tk.Frame(contentFrame, bg = "#cccccc")
        self.productFrame.place(x=20, y=160, width=970, height=440)

        searchBar = ttk.Entry(contentFrame, font = ('Helvetica', 10))
        searchBar.place(x=780, y=125, width=210, height=25)

        category_name_list = ['Category']
        for i in range(len(self.homeController.category.get_category_list())):
            category_name_list.append(self.homeController.category.get_category_list()[i][0])

        categoryDrop = ttk.Combobox(contentFrame, values = category_name_list, font = ('Helvetica', 10), state = "r")
        categoryDrop.set("Category")
        categoryDrop.place(x=580, y=125, width=90, height=25)

        brand_name_list = ['Brand']
        for i in range(len(self.homeController.brand.get_brand_list())):
            brand_name_list.append(self.homeController.brand.get_brand_list()[i][0])
        brandDrop = ttk.Combobox(contentFrame, values=brand_name_list, font = ('Helvetica', 10), state = "r")
        brandDrop.set("Brand")
        brandDrop.place(x=680, y=125, width=90, height=25)

        sortDrop = ttk.Combobox(contentFrame,values=['Sort', 'Name', 'Selling_Price_M'] , font = ('Helvetica', 10), state = "r")
        sortDrop.set("Sort")
        sortDrop.place(x=480, y=125, width=90, height=25)

        # Treeview
        self.tree = self.homeController.showTreeView_ProductList(contentFrame, self.productFrame, searchBar.get(), sortDrop.get(), categoryDrop.get(), brandDrop.get())
        def searchByContent(e):
            self.tree = self.homeController.showTreeView_ProductList(contentFrame, self.productFrame, searchBar.get(), sortDrop.get(), categoryDrop.get(), brandDrop.get())
            return self.tree
        searchBar.bind('<KeyRelease>', searchByContent)

        sortDrop.bind("<<ComboboxSelected>>", searchByContent)
        brandDrop.bind("<<ComboboxSelected>>", searchByContent)
        categoryDrop.bind("<<ComboboxSelected>>", searchByContent)

    def displayManageProductsByCategory(self, category):
        contentFrame = self.contentFrame
        try:
            self.tree.destroy()
        except:
            pass
        clearFrame(contentFrame)
        tk.Label(contentFrame, text="Manage products",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        tk.Frame(contentFrame, width=10, height=24, bg='#cc0000').place(x=48, y=70)

        self.productFrame = tk.Frame(contentFrame, bg = "#cccccc")
        self.productFrame.place(x=20, y=160, width=970, height=440)

        searchBar = ttk.Entry(contentFrame, font = ('Helvetica', 10))
        searchBar.place(x=780, y=125, width=210, height=25)

        category_name_list = ['Category']
        for i in range(len(self.homeController.category.get_category_list())):
            category_name_list.append(self.homeController.category.get_category_list()[i][0])

        categoryDrop = ttk.Combobox(contentFrame, values = category_name_list, font = ('Helvetica', 10), state = "r")
        categoryDrop.set(category)
        categoryDrop.place(x=580, y=125, width=90, height=25)

        brand_name_list = ['Brand']
        for i in range(len(self.homeController.brand.get_brand_list())):
            brand_name_list.append(self.homeController.brand.get_brand_list()[i][0])
        brandDrop = ttk.Combobox(contentFrame, values=brand_name_list, font = ('Helvetica', 10), state = "r")
        brandDrop.set("Brand")
        brandDrop.place(x=680, y=125, width=90, height=25)

        sortDrop = ttk.Combobox(contentFrame,values=['Sort','Name', 'Selling_Price_M'] , font = ('Helvetica', 10), state = "r")
        sortDrop.set("Sort")
        sortDrop.place(x=480, y=125, width=90, height=25)

        # Treeview
        self.tree = self.homeController.showTreeView_ProductList(contentFrame, self.productFrame, searchBar.get(), sortDrop.get(), categoryDrop.get(), brandDrop.get())
        def searchByContent(e):
            self.tree = self.homeController.showTreeView_ProductList(contentFrame, self.productFrame, searchBar.get(), sortDrop.get(), categoryDrop.get(), brandDrop.get())
            return self.tree
        searchBar.bind('<KeyRelease>', searchByContent)

        sortDrop.bind("<<ComboboxSelected>>", searchByContent)
        brandDrop.bind("<<ComboboxSelected>>", searchByContent)
        categoryDrop.bind("<<ComboboxSelected>>", searchByContent)