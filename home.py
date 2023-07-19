from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import sys
import os
import databaseInitialization as dbi
from SampleEntriesCreation import initialize_database


# 6 rows, 5 columns
title = "Homepage"
add_remove_worker = "Add/Remove Worker"
daily = "Daily Worker Entry"
monthly = "Monthly Worker Entry"
get_data = "Get Data"
worker_contact = "Worker Contact Details"
task_list = "Add or Remove Tasks"
font1 = ('Times 24')


class Application(Frame):
    global py_version
    py_version = sys.version_info[0]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        dbi.init_db_if_not_already_created()
        self.display()

    def callback_AR(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "AddRemove.py")
        if py_version == 2:
            os.system("python3 \"" + script_path + "\"")
        else:
            os.system("python \"" + script_path + "\"")

    def callback_DE(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DailyWorkerEntry.py")
        if py_version == 2:
            os.system("python3 \"" + script_path + "\"")
        else:
            os.system("python \"" + script_path + "\"")

    def callback_ME(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "MonthlyEntry.py")
        if py_version == 2:
            os.system("python3 \"" + script_path + "\"")
        else:
            os.system("python \"" + script_path + "\"")

    def callback_GD(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "GetData.py")
        if py_version == 2:
            os.system("python3 \"" + script_path + "\"")
        else:
            os.system("python \"" + script_path + "\"")

    def callback_WD(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "WorkerDetails.py")
        if py_version == 2:
            os.system("python3 \"" + script_path + "\"")
        else:
            os.system("python \"" + script_path + "\"")

    def callback_TL(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "AddRemoveTasks.py")
        if py_version == 2:
            os.system("python3 \"" + script_path + "\"")
        else:
            os.system("python \"" + script_path + "\"")

    def add_buttons(self):
        self.btn1 = Button(self.master, text = add_remove_worker, command=self.callback_AR, width=25).grid(row=2, column=1, sticky="EW")
        self.btn2 = Button(self.master, text = daily, command=self.callback_DE, width=25).grid(row=2, column=3, sticky="EW")
        self.btn3 = Button(self.master, text=monthly, command=self.callback_ME, width=25).grid(row=2, column=5, sticky="EW")
        self.btn4 = Button(self.master, text=get_data, command=self.callback_GD, width=25).grid(row=4, column=1, sticky="EW")
        self.btn5 = Button(self.master, text=worker_contact, command=self.callback_WD, width=25).grid(row=4, column=3, sticky="EW")
        self.btn6 = Button(self.master, text=task_list, command=self.callback_TL, width=25).grid(row=4, column=5, sticky="EW")
        
    def add_labels(self):
        self.l1 = Label(self.master, anchor="center", text=title, font=font1).grid(row=0, column=1, columnspan=5)

    def setup_window(self, root):
        Grid.rowconfigure(root, index = 0, weight = 1)
        Grid.rowconfigure(root, index = 1, weight = 1)
        Grid.rowconfigure(root, index = 2, weight = 1)
        Grid.rowconfigure(root, index = 3, weight = 1)
        Grid.rowconfigure(root, index = 4, weight = 1)
        Grid.rowconfigure(root, index = 5, weight = 1)
        Grid.rowconfigure(root, index = 6, weight = 1)
        Grid.columnconfigure(root, index = 0, weight = 1)
        Grid.columnconfigure(root, index = 1, weight = 1)
        Grid.columnconfigure(root, index = 2, weight = 1)
        Grid.columnconfigure(root, index = 3, weight = 1)
        Grid.columnconfigure(root, index = 4, weight = 1)
        Grid.columnconfigure(root, index = 5, weight = 1)
        Grid.columnconfigure(root, index = 6, weight = 1)
        root.columnconfigure(6, minsize=20)
        root.columnconfigure(0, minsize=20)

    def display(self):
        self.winfo_toplevel().title("Labourer Management System")
        self.setup_window(root)
        self.add_labels()
        self.add_buttons()

if __name__ == "__main__":
    dbi.init_db_if_not_already_created()
    if str(input("Would you like to initialize the database with pre-made entries? \nEnter yes or no: ")).lower() == 'yes':
        initialize_database()
    root = Tk()
    root.geometry("800x300")
    app = Application(master = root)
    print(root.winfo_screenheight())
    print(root.winfo_screenwidth())
    app.mainloop()
