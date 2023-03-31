from views.login_page import MainApplication
import os

if __name__ == "__main__":
    app = MainApplication()
    file_name = "img/icon.ico"
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    app.iconbitmap(file_path)
    app.title("Motorbike Management System")
    app.mainloop()