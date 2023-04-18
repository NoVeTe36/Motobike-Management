import tkinter as tk
from tkinter import messagebox
import datetime
from views.View import View
from db.settingup import SettingUp
from views.gifthreading import *
from views.Trivial import *
from views.mainviews import AddProductView, BrandView, CategoryView, DashboardView, NewOrderView, ManageOrdersView, ManageProductsView, AddProductView, UserView

class HomeView(tk.Tk, View):
    def __init__(self,controller, root, user):
        SettingUp()
        self.window = root
        self.homeController = controller
        self.user = user
        self.window.geometry("1280x720+100+50")
        self.window.resizable(False, False)
        self.window.title("Motorcycle Store Information Management System")
        self.window.bind("<Control-w>", lambda e: self.window.destroy())

        userInformationFrame = tk.Frame(self.window, width=1280, height=60, bg="black")
        userInformationFrame.place(x=0, y=0)

        userBtn = HoverButton(userInformationFrame, bg = "#000000", fg = "#ffffff", text = self.user, font=('Helvetica', 14), bd=None, activebackground='#000000', activeforeground = 'white', relief='flat', command = lambda: UserView.UserView(self.contentFrame, self.homeController, self.user, self.window).displayUser(), cursor = 'hand2')
        userBtn.place(x=1160, y = 20, width = 100, height = 20)

        navigationFrame = tk.Frame(self.window, width=270, height=660, bg="#cc0000")
        navigationFrame.place(x=0, y=60)

        self.contentFrame = tk.Frame(self.window, width=1010, height=660, bg='#fff')
        self.contentFrame.place(x=270, y=60)

        move_Frame = tk.Frame(self.window, width=180, height=120, bg='#cc0000')
        move_Frame.place(x=0, y=-90)

        self.gif_thread1 = GifThread(self.window, move_Frame, 12, '../img/login_page.gif', -50, -40, "#cc0000")
        self.gif_thread1.run()


        dashboardBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Dashboard", font=('Helvetica', 15, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: DashboardView.DashboardView(self.contentFrame, self.homeController, self.user, self.window).displayDashboard(), cursor = 'hand2')
        dashboardBtn.place(x=-25, y=160)

        # Button to activate the function
        brandBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Brand", font=('Helvetica', 15, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: BrandView.BrandView(self.contentFrame, self.homeController, self.user, self.window).displayBrand(), cursor = 'hand2')
        brandBtn.place(x=-27, y=205)

        categoryBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Category", font=('Helvetica', 15, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: CategoryView.CategoryView(self.contentFrame, self.homeController, self.user, self.window).displayCategory(), cursor = 'hand2')
        categoryBtn.place(x=-27, y=250)

        addProductBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Add Product", font=('Helvetica', 15, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: AddProductView.AddProductView(self.contentFrame, self.homeController, self.user, self.window).displayAddProduct(), cursor = 'hand2')
        addProductBtn.place(x=-25, y=295)

        manageProductsBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Manage Products", font=('Helvetica', 15, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: ManageProductsView.ManageProductsView(self.contentFrame, self.homeController, self.user, self.window).displayManageProducts(), cursor = 'hand2')
        manageProductsBtn.place(x=-21, y=340)

        newOrderBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="New order", font=('Helvetica', 15, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: NewOrderView.NewOrderView(self.contentFrame, self.homeController, self.user, self.window).displayNewOrder(), cursor = 'hand2')
        newOrderBtn.place(x=-27, y=385)

        manageOrdersBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Orders history", font=('Helvetica', 15, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: ManageOrdersView.ManageOrdersView(self.contentFrame, self.homeController, self.user, self.window).displayManageOrders(), cursor = 'hand2')
        manageOrdersBtn.place(x=-27, y=430)

        # bind the function to the button <Button-1> is the left mouse button yesno messagebox
        logoutBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Logout", font=('Helvetica', 15, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.logout(), cursor = 'hand2')
        logoutBtn.place(x= -27, y = 580)

        self.user_info = self.homeController.take_info(self.user)

        DashboardView.DashboardView(self.contentFrame, self.homeController, self.user, self.window).displayDashboard()
        move_in(move_Frame)

    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.window.destroy()
            self.homeController.openLoginPage()

    
    def calendar(self, contentFrame, username):
        # Get today's date
        today = datetime.datetime.today().date()

        # Get login history for the user
        login_history = self.homeController.get_login_history(username)
        print(login_history)

    def main(self):
        self.mainloop()

    def close(self):
        return