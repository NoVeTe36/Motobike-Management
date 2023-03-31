from core.Controller import Controller
from core.Core import Core
from models.Product import Product
from tkinter import messagebox
from models.Brand import Brand
import tkinter as tk
from tkinter import ttk

"""
    Main controller. It will be responsible for program's main screen behavior.
"""
class HomeController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self,root):
        self.homeView = self.loadView("Home",root)
        self.brand = Brand()
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    product = Product()
#DASHBOARD

    def get_sum_product(self):
        return str(self.product.get_sum_product())
    def get_sum_brand(self):
        return str(self.product.get_sum_brand())
    def get_sum_soldproduct(self):
        return str(self.product.get_sum_product())
    def get_profit(self):
        return str(self.product.get_sum_product())

#ADD_BRAND    
    def btnAdd_Brand(self,entry, tree, contentFrame):
        brand_list = []
        response = self.product.add_brand(entry)
        if response > 0:           
            messagebox.showinfo("Add brand", "Customer successfully added!")
            brand_name = entry.get()
            self.brand.add(brand_name)
        else: 
            messagebox.showerror("Add brand", "Error while adding customer")
        entry.delete(0, 'end')
        self.reset_BrandList(tree, self.BrandList_added(self.get_brand_list(), entry.get()), contentFrame)

#DISPLAY_BRAND_LIST
    def showTreeView_BrandList(self, contentFrame, brand_list):
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        tree = ttk.Treeview(contentFrame, height=15)
        tree["columns"] = ("brand")
        tree.column("#0", width=150, minwidth=50, stretch=False)
        tree.column("brand", width=730, minwidth=200, stretch=False)
        tree.heading("#0", text="No.")
        tree.heading("brand", text="Brand")
        tree.place(x=60, y=290)
        for i in range(len(brand_list)):
            tree.insert("", i, text=i+1, values=(brand_list[i],))
        # Scrollbar
        scrollBar = ttk.Scrollbar(contentFrame, orient="vertical", command=tree.yview)
        scrollBar.place(x=950, y=290, height=300)
        tree.configure(yscrollcommand=scrollBar.set)
        return tree
    
    def reset_BrandList(self, tree, brand_list, contentFrame):
        tree.destroy()
        tree = self.showTreeView_BrandList(contentFrame, brand_list)


    def BrandList_added(self, brand_list, brand):
        brand_list.append(brand)
        return brand_list
    
    def display_brand(self):
        return self.product.display_brand()

    def get_brand_list(self):
        brand_list = []
        for i in range(len(self.brand.get_brand_list())):
            brand_list.append(self.brand.get_brand_list()[i][0])
        return brand_list       

#ADD_PRODUCT (can linked voi DB):
    def btnAdd_Product(self, fields):
        product = []
        response = self.product.add_product(fields)
        if response > 0:           
            messagebox.showinfo("Add brand", "Customer successfully added!")
            for i in range(len(fields)):
                product.append(fields[i].get())
 #           self.brand.add(product)
        else: 
            messagebox.showerror("Add brand", "Error while adding customer")
        for i in range(len(fields)):
            fields[i].delete = (0, 'end')   
    def clearContent(self, fields):
        for i in range(len(fields)):
            fields[i].delete = (0, 'end')                 
    
    """
        @Override
    """
    def main(self):
        self.homeView.main()