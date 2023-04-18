import tkinter as tk
from tkinter import ttk
from views.gifthreading import *
from views.Trivial import *

class NewOrderView:
    def __init__(self, contentFrame, controller, user, root):
        self.homeController = controller
        self.window = root
        self.user = user
        self.contentFrame = contentFrame
        self.user_info = self.homeController.take_info(self.user)

    def displayNewOrder(self):
        contentFrame = self.contentFrame
        clearFrame(contentFrame)
        Field = []
        tk.Label(contentFrame, text="New order",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        tk.Frame(contentFrame, width=10, height=24, bg='#cc0000').place(x=48, y=70)

        customerInformationFrame = tk.Frame(contentFrame, height=180, width=890, bg='#cccccc')
        customerInformationFrame.place(x=60, y=120)
        tk.Label(customerInformationFrame, text="Customer Information:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=10, y=10)

        tk.Label(customerInformationFrame, text="Name:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=40, y=60)
        customerNameInput = ttk.Entry(customerInformationFrame, width=22, font=('Helvetica', 14))
        customerNameInput.place(x=150,y=60)
        Field.append(customerNameInput)

        tk.Label(customerInformationFrame, text="Phone:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=40, y=120)
        phoneInput = ttk.Entry(customerInformationFrame, width=22, font=('Helvetica', 14))
        phoneInput.place(x=150,y=120)
        Field.append(phoneInput)

        modelInformationFrame = tk.Frame(contentFrame, height=290, width=890, bg='#cccccc')
        modelInformationFrame.place(x=60, y=330)
        tk.Label(modelInformationFrame, text="Product bought:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=10, y=10)
        
        # productInput = ttk.Entry(tempFrame, width=50, font=('Helvetica', 14))
        # productInput.place(x=100,y=0)

        tempFrame = tk.Frame(contentFrame, height=80, width=400, bg='#cccccc')
        tempFrame.place(x=500, y=200)
        tk.Label(tempFrame, text="Product:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=0,y=0)
        
        productInput = ttk.Entry(tempFrame, width=50, font=('Helvetica', 14))
        productInput.place(x=100,y=0)
        productInput.configure(state="disabled")

        def clearContent():
            customerNameInput.delete(0, 'end')
            phoneInput.delete(0, 'end')

        searchBar = ttk.Entry(contentFrame, font = ('Helvetica', 10))
        searchBar.place(x=690, y=345, width=210, height=25)

        self.tree = self.homeController.showTreeView_OrderProductList(contentFrame, productInput, searchBar.get())
        def searchByName(e):
            self.tree = self.homeController.showTreeView_OrderProductList(contentFrame, productInput, searchBar.get())
            return self.tree
        searchBar.bind('<KeyRelease>', searchByName)

        clearBtn = HoverButton(modelInformationFrame,text='Clear',bg='#cc0000', fg='#fff', font=('Helvetica', 10, 'bold'), width=10, activebackground='#cc0000', activeforeground='#fff', relief='flat', command=clearContent)
        clearBtn.place(x=690, y=250)

        addBtn = HoverButton(modelInformationFrame,text='Add',bg='#238636', fg='#fff', font=('Helvetica', 10, 'bold'), width=10, activebackground='#238636', activeforeground='#fff', relief='flat', command=lambda: self.homeController.btnAdd_Order(Field, tempFrame, contentFrame, productInput, self.tree))
        addBtn.place(x=790,y=250)