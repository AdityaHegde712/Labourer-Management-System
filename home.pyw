from tkinter import *
from tkinter.ttk import *
import sys
import os
import databaseInitialization as dbi
import subprocess
from translate import Translator
import worker as w
import tasks
import dailyEntries as de
import attendance

# 6 rows, 5 columns
title = "Homepage"
add_remove_worker = "Add/Remove Worker"
daily = "Daily Worker Entry"
monthly = "Monthly Worker Entry"
get_data = "Get Data"
worker_contact = "Worker Contact Details"
task_list = "Add or Remove Tasks"
font1 = ('Times 24')
buttonfont = ('Times 20')
add_entries = "Add Sample Entries"


class Application(Frame):
    global py_version
    py_version = sys.version_info[0]

    def initialize_database(self):
        # Enter workers list
        workers = [
            {
                'name': 'John Smith',
                'phone_no': '1234567890'
            },
            {
                'name': 'Emma Johnson',
                'phone_no': '9876543210'
            },
            {
                'name': 'Michael Davis',
                'phone_no': '4567890123'
            },
            {
                'name': 'Sophia Wilson',
                'phone_no': '8901234567'
            },
            {
                'name': 'Daniel Thompson',
                'phone_no': '2345678901'
            },
            {
                'name': 'Olivia Martinez',
                'phone_no': '9012345678'
            },
            {
                'name': 'William Anderson',
                'phone_no': '3456789012'
            },
            {
                'name': 'Ava Taylor',
                'phone_no': '7890123456'
            },
            {
                'name': 'David Hernandez',
                'phone_no': '5678901234'
            },
            {
                'name': 'Mia Moore',
                'phone_no': '0123456789'
            }
        ]
        for entry in workers:
            w.insert_one(entry)


        # Sample Daily Entries
        sample_daily_entries = [
            {
                'name': 'Michael Davis',
                'phone_no': '4567890123',
                'task': 'Cleaning animal pens',
                'wage': 162,
                'date': '2023-06-03'
            },
            {
                'name': 'David Hernandez',
                'phone_no': '5678901234',
                'task': 'Milking cows',
                'wage': 173,
                'date': '2023-06-12'
            },
            {
                'name': 'David Hernandez',
                'phone_no': '5678901234',
                'task': 'Plowing fields',
                'wage': 133,
                'date': '2023-06-19'
            },
            {
                'name': 'Olivia Martinez',
                'phone_no': '9012345678',
                'task': 'Planting seeds',
                'wage': 149,
                'date': '2023-06-06'
            },
            {
                'name': 'Mia Moore',
                'phone_no': '0123456789',
                'task': 'Plowing fields',
                'wage': 70,
                'date': '2023-06-29'
            },
            {
                'name': 'Ava Taylor',
                'phone_no': '7890123456',
                'task': 'Plowing fields',
                'wage': 167,
                'date': '2023-06-15'
            },
            {
                'name': 'Olivia Martinez',
                'phone_no': '9012345678',
                'task': 'Pruning fruit trees',
                'wage': 148,
                'date': '2023-06-07'
            },
            {
                'name': 'Michael Davis',
                'phone_no': '4567890123',
                'task': 'Gathering eggs',
                'wage': 146,
                'date': '2023-06-04'
            },
            {
                'name': 'John Smith',
                'phone_no': '1234567890',
                'task': 'Planting seeds',
                'wage': 51,
                'date': '2023-06-26'
            },
            {
                'name': 'David Hernandez',
                'phone_no': '5678901234',
                'task': 'Pruning fruit trees',
                'wage': 84,
                'date': '2023-06-23'
            },
            {
                'name': 'Michael Davis',
                'phone_no': '4567890123',
                'task': 'Harvesting vegetables',
                'wage': 144,
                'date': '2023-06-30'
            },
            {
                'name': 'Daniel Thompson',
                'phone_no': '2345678901',
                'task': 'Fertilizing fields',
                'wage': 71,
                'date': '2023-06-28'
            },
            {
                'name': 'Ava Taylor',
                'phone_no': '7890123456',
                'task': 'Weeding',
                'wage': 101,
                'date': '2023-06-27'
            },
            {
                'name': 'Ava Taylor',
                'phone_no': '7890123456',
                'task': 'Maintaining farm equipment',
                'wage': 93,
                'date': '2023-06-08'
            },
            {
                'name': 'William Anderson',
                'phone_no': '3456789012',
                'task': 'Repairing fences',
                'wage': 82,
                'date': '2023-06-03'
            }
        ]
        for entry in sample_daily_entries:
            de.insert_one(entry)


        sample_monthly_entries = [
            {'date': '2023-06-01', 'task': 'Planting seeds', 'wage': 212, 'worker_id': 1},
            {'date': '2023-06-02', 'task': 'Plowing fields', 'wage': 100, 'worker_id': 2}, 
            {'date': '2023-06-03', 'task': 'Cleaning animal pens', 'wage': 206, 'worker_id': 1},
            {'date': '2023-06-04', 'task': 'Gathering eggs', 'wage': 257, 'worker_id': 8},
            {'date': '2023-06-05', 'task': 'Cleaning animal pens', 'wage': 117, 'worker_id': 3},
            {'date': '2023-06-06', 'task': 'Planting seeds', 'wage': 261, 'worker_id': 4},
            {'date': '2023-06-07', 'task': 'Pruning fruit trees', 'wage': 259, 'worker_id': 7},
            {'date': '2023-06-08', 'task': 'Gathering eggs', 'wage': 211, 'worker_id': 4},
            {'date': '2023-06-09', 'task': 'Milking cows', 'wage': 65, 'worker_id': 5},
            {'date': '2023-06-10', 'task': 'Pruning fruit trees', 'wage': 238, 'worker_id': 6},
            {'date': '2023-06-11', 'task': 'Planting seeds', 'wage': 215, 'worker_id': 7},
            {'date': '2023-06-12', 'task': 'Milking cows', 'wage': 289, 'worker_id': 2},
            {'date': '2023-06-13', 'task': 'Plowing fields', 'wage': 62, 'worker_id': 8},
            {'date': '2023-06-14', 'task': 'Cleaning animal pens', 'wage': 211, 'worker_id': 9},
            {'date': '2023-06-15', 'task': 'Plowing fields', 'wage': 243, 'worker_id': 6},
            {'date': '2023-06-16', 'task': 'Gathering eggs', 'wage': 52, 'worker_id': 10},
            {'date': '2023-06-19', 'task': 'Plowing fields', 'wage': 227, 'worker_id': 3},
            {'date': '2023-06-23', 'task': 'Pruning fruit trees', 'wage': 134, 'worker_id': 10},
            {'date': '2023-06-26', 'task': 'Planting seeds', 'wage': 101, 'worker_id': 9},
            {'date': '2023-06-29', 'task': 'Plowing fields', 'wage': 149, 'worker_id': 5}
        ]
        for entry in sample_monthly_entries:
            attendance.insert_one(entry)


        # Sample Activity list
        task_list = [
            "Planting seeds",
            "Watering crops",
            "Weeding",
            "Fertilizing fields",
            "Harvesting vegetables",
            "Pruning fruit trees",
            "Milking cows",
            "Feeding livestock",
            "Cleaning animal pens",
            "Repairing fences",
            "Plowing fields",
            "Maintaining farm equipment",
            "Herding sheep",
            "Gathering eggs",
            "Applying pest control"
        ]
        for task in task_list:
            tasks.insert_one(task)

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.display()

    def callback_AR(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "AddRemove.pyw")
        subprocess.Popen(["pythonw", script_path], creationflags=subprocess.CREATE_NO_WINDOW)

    def callback_DE(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DailyWorkerEntry.pyw")
        subprocess.Popen(["pythonw", script_path], creationflags=subprocess.CREATE_NO_WINDOW)

    def callback_ME(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "MonthlyEntry.pyw")
        subprocess.Popen(["pythonw", script_path], creationflags=subprocess.CREATE_NO_WINDOW)

    def callback_GD(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "GetData.pyw")
        subprocess.Popen(["pythonw", script_path], creationflags=subprocess.CREATE_NO_WINDOW)

    def callback_WD(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "WorkerDetails.pyw")
        subprocess.Popen(["pythonw", script_path], creationflags=subprocess.CREATE_NO_WINDOW)

    def callback_TL(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "AddRemoveTasks.pyw")
        subprocess.Popen(["pythonw", script_path], creationflags=subprocess.CREATE_NO_WINDOW)

    def add_buttons(self):
        self.btn1 = Button(self.master, text = add_remove_worker, command=self.callback_AR, width=25).grid(row=2, column=1, sticky="EW")
        self.btn2 = Button(self.master, text = daily, command=self.callback_DE, width=25).grid(row=2, column=3, sticky="EW")
        self.btn3 = Button(self.master, text=monthly, command=self.callback_ME, width=25).grid(row=2, column=5, sticky="EW")
        self.btn4 = Button(self.master, text=get_data, command=self.callback_GD, width=25).grid(row=4, column=1, sticky="EW")
        self.btn5 = Button(self.master, text=worker_contact, command=self.callback_WD, width=25).grid(row=4, column=3, sticky="EW")
        self.btn6 = Button(self.master, text=task_list, command=self.callback_TL, width=25).grid(row=4, column=5, sticky="EW")
        self.btn6 = Button(self.master, text=add_entries, command=self.initialize_database, width=25).grid(row=6, column=3, sticky="EW")
        # self.btn7 = Button(self.master, text="Telugu", command=lambda: self.translate_to_telugu, width=15).grid(row=7, column=5, sticky=E)
        self.btn7 = Button(self.master, text="Telugu", command=self.translate_to_telugu, width=15)
        self.btn7.place(relx=0.87, rely=0.85)
        self.btn8 = Button(self.master, text="Kannada", command=self.translate_to_kannada, width=15)
        self.btn8.place(relx=0.87, rely=0.92)

        
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
        Grid.rowconfigure(root, index = 7, weight = 1)
        Grid.rowconfigure(root, index = 8, weight = 1)
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

    def translate_to_telugu(self):
        translator = Translator(from_lang='en', to_lang='te')
        translated_text = ""
        # Get all the text contents of the window
        for child in self.master.winfo_children():
            if isinstance(child, (Label, Button)):
                # Translate the text using the translate module
                translation = translator.translate(child['text'])
                translated_text += translation + '\n'
                # Update the translated text to Telugu
                child['text'] = translation
        self.btn7.destroy()
        self.btn8.destroy()

    def translate_to_kannada(self):
        translator = Translator(from_lang='en', to_lang='kn')
        translated_text = ""
        # Get all the text contents of the window
        for child in self.master.winfo_children():
            if isinstance(child, (Label, Button)):
                # Translate the text using the translate module
                translation = translator.translate(child['text'])
                translated_text += translation + '\n'
                # Update the translated text to Kannada
                child['text'] = translation
        self.btn7.destroy()
        self.btn8.destroy()

if __name__ == "__main__":
    dbi.init_db_if_not_already_created()
    root = Tk()
    root.geometry("900x500")
    app = Application(master = root)
    app.mainloop()
