import tkinter as tk
from tkinter import ttk
from views.gifthreading import *
from views.Trivial import *

class AddProductView:
    def __init__(self, contentFrame, controller, user, root):
        self.homeController = controller
        self.window = root
        self.user = user
        self.contentFrame = contentFrame
        self.user_info = self.homeController.take_info(self.user)

    def displayAddProduct(self):
        contentFrame = self.contentFrame
        clearFrame(contentFrame)
        Field = []
        tk.Label(contentFrame, text="Add product",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        tk.Frame(contentFrame, width=10, height=24, bg='#cc0000').place(x=48, y=70)
        inputFrame = tk.Frame(contentFrame, width=890, height=470, bg='#cccccc')
        inputFrame.place(x=60, y=120)

        # Input for model name
        tk.Label(inputFrame, text="Model:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=30)
        modelInput = ttk.Entry(inputFrame, width=66, font=('Helvetica', 14))
        modelInput.place(x=120,y=30)
        Field.append(modelInput)

        # Options for brand
        tk.Label(inputFrame, text="Brand:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=80)
        brand_name_list = []
        for i in range(len(self.homeController.brand.get_brand_list())):
            brand_name_list.append(self.homeController.brand.get_brand_list()[i][0])
        brandOption = ttk.Combobox(inputFrame, width= 24, font=('Helvetica', 14), values=brand_name_list, state='r')
        brandOption.place(x=120, y=80)
        Field.append(brandOption)

        # Options for category
        tk.Label(inputFrame, text="Category:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=450, y=80)
        category_name_list = []
        for i in range(len(self.homeController.category.get_category_list())):
            category_name_list.append(self.homeController.category.get_category_list()[i][0])
        categoryOption = ttk.Combobox(inputFrame, width=24, font=('Helvetica', 14), values=category_name_list, state='r')
        categoryOption.place(x=570, y=80)
        Field.append(categoryOption)

        # Input for length
        tk.Label(inputFrame, text="Length:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=130)
        lengthInput = ttk.Entry(inputFrame, width=6, font=('Helvetica', 14))
        lengthInput.place(x=120,y=130)
        Field.append(lengthInput)

        # Input for width
        tk.Label(inputFrame, text="Width:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=250, y=130)
        widthInput = ttk.Entry(inputFrame, width=6, font=('Helvetica', 14))
        widthInput.place(x=330,y=130)
        Field.append(widthInput)

        # Input for height
        tk.Label(inputFrame, text="Height:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=450, y=130)
        heightInput = ttk.Entry(inputFrame, width=6, font=('Helvetica', 14))
        heightInput.place(x=535,y=130)
        Field.append(heightInput)

        # Input mass
        tk.Label(inputFrame, text="Mass:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=700, y=130)
        massInput = ttk.Entry(inputFrame, width=6, font=('Helvetica', 14))
        massInput.place(x=780,y=130)
        Field.append(massInput)

        # Input fuel capacity
        tk.Label(inputFrame, text="Fuel Capacity:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=180)
        fuelCapacityInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        fuelCapacityInput.place(x=230,y=180)
        Field.append(fuelCapacityInput)

        # Input fuel consumption
        tk.Label(inputFrame, text="Fuel Consumption:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=450, y=180)
        fuelConsumptionInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        fuelConsumptionInput.place(x=680,y=180)
        Field.append(fuelConsumptionInput)

        # Input engine type
        tk.Label(inputFrame, text="Engine type:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=230)
        engineTypeInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        engineTypeInput.place(x=230,y=230)
        Field.append(engineTypeInput)

        # Input maximal efficiency
        tk.Label(inputFrame, text="Maximal Efficiency:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=450, y=230)
        maximalEfficiencyInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        maximalEfficiencyInput.place(x=680,y=230)
        Field.append(maximalEfficiencyInput)

        # Input color
        tk.Label(inputFrame, text="Color:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=280)
        colorInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        colorInput.place(x=230,y=280)
        Field.append(colorInput)

        # Input selling price
        tk.Label(inputFrame, text="Selling price(M):",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=330)
        sellingPriceInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        sellingPriceInput.place(x=230,y=330)
        Field.append(sellingPriceInput)

        tk.Label(inputFrame, text="Quantity:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=380)
        quantityInput = ttk.Entry(inputFrame, width=7, font=('Helvetica', 14))
        quantityInput.place(x=230,y=380)
        Field.append(quantityInput)

        addBtn = HoverButton(inputFrame,text='Add',bg='#238636', fg='#fff', font=('Helvetica', 10, 'bold'), width=10, activebackground='#238636', activeforeground='#fff', relief='flat', command = lambda: self.homeController.btnAdd_Product(Field))
        addBtn.place(x=670, y = 420)

        # Clear button
        clearBtn = HoverButton(inputFrame,text='Clear',bg='#cc0000', fg='#fff', font=('Helvetica', 10, 'bold'), width=10, activebackground='#cc0000', activeforeground='#fff', relief='flat', command = lambda: self.homeController.clearContent(Field))
        clearBtn.place(x=770,y=420)

    