from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import DateEntry
from PIL import ImageTk, Image
import worker as w
import os
import attendance
import tasks as t
import sys

title = "Regular Worker Entry"
label1 = "Date"
label2 = "Name"
label3 = "Activity"
label4 = "Day's Wage"
title_font = ('Times 24')
label_font = ('Arial 12')


class Application(Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.Task_Name = StringVar()
            self.Task_Name.set("Select Task")
            self.display()
        
        def get_worker_id_from_name(self, all_workers, name):
            for entry in all_workers:
                if entry['name'] == name:
                    return entry['id']
        
        def get_selected_date(self):
            selected_date = self.date_picker.get_date()
            print(f"Selected Date: {selected_date}")
        
        def refresh_page(self):
            entry = {
                'date': str(self.date_picker.get_date()),
                'task': str(self.activity_entry.get()),
                'wage': int(self.wage_entry.get()),
                'worker_id': int(self.get_worker_id_from_name(w.select_all(), str(self.name_entry.get())))
            }
            attendance.insert_one(entry)
            self.name_entry.delete(0, END)
            self.activity_entry.delete(0, END)
            self.wage_entry.delete(0, END)
            self.Task_Name.set("Select Task")
            self.date_picker = DateEntry(self.master, width=16, background="dark grey",
                                     foreground="white", borderwidth=2)
            self.date_picker.grid(row=2, column=1, padx=10, pady=10)
        
        def add_widgets(self):

            def open_file():
                root.destroy()

            # Labels
            self.l1 = Label(self.master, anchor="center", text=title, font=title_font).grid(row=0, column=1, columnspan=7)
            self.l2 = Label(self.master, anchor="center", text=label1, font=label_font).grid(row=1, column=1, sticky=S)
            self.l3 = Label(self.master, anchor="center", text=label2, font=label_font).grid(row=1, column=3, sticky=S)
            self.l4 = Label(self.master, anchor="center", text=label3, font=label_font).grid(row=1, column=5, sticky=S)
            self.l5 = Label(self.master, anchor="center", text=label4, font=label_font).grid(row=1, column=7, sticky=S)

            # Buttons and Entries
            self.date_picker = DateEntry(self.master, width=16, background="dark grey",
                                     foreground="white", borderwidth=2)
            self.date_picker.grid(row=2, column=1, padx=10, pady=10)

            self.date_btn = ttk.Button(self.master, text="Select Date", command=self.get_selected_date, style="TButton")
            self.date_btn.grid(row=3, column=1, padx=10, pady=10, sticky=N)

            self.name_entry = Entry(self.master, width=20)
            self.name_entry.grid(row=2, column=3)

            # CHOOSE ACTIVITY
            tasks = t.fetch_all()
            for task in tasks:
                tasks[tasks.index(task)] = task[0]
            self.activity_entry = ttk.Combobox(self.master, textvariable=self.Task_Name, values=tasks, state="readonly", font=6)
            self.activity_entry.grid(row=2, column=5)

            self.wage_entry = Entry(self.master, width=10)
            self.wage_entry.grid(row=2, column=7)

            self.submit_button = ttk.Button(self.master, text="Add Entry", command=self.refresh_page)
            self.submit_button.grid(row=4, column=8)

            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, "Home.png")
            image = Image.open(image_path)
            image = image.resize((50, 50))  # Resize the image as needed
            photo = ImageTk.PhotoImage(image)

            self.button = Button(self.master, image=photo, command=open_file)
            self.button.image = photo  # Store a reference to the image to prevent garbage collection
            self.button.grid(row=0, column=0)

        def setup_window(self, root):
            Grid.rowconfigure(root, index = 0, weight = 1)
            Grid.rowconfigure(root, index = 1, weight = 1)
            Grid.rowconfigure(root, index = 2, weight = 1)
            Grid.rowconfigure(root, index = 3, weight = 1)
            Grid.rowconfigure(root, index = 4, weight = 1)
            Grid.columnconfigure(root, index = 0, weight = 1)
            Grid.columnconfigure(root, index = 1, weight = 1)
            Grid.columnconfigure(root, index = 2, weight = 1)
            Grid.columnconfigure(root, index = 3, weight = 1)
            Grid.columnconfigure(root, index = 4, weight = 1)
            Grid.columnconfigure(root, index = 5, weight = 1)
            Grid.columnconfigure(root, index = 6, weight = 1)
            Grid.columnconfigure(root, index = 7, weight = 1)
            Grid.columnconfigure(root, index = 8, weight = 1)
            root.columnconfigure(8, minsize=20)
            root.columnconfigure(0, minsize=20)

        def display(self):
            self.winfo_toplevel().title("Labourer Management System")
            self.setup_window(root)
            self.add_widgets()


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x300")
    app = Application(master = root)
    print(root.winfo_screenheight())
    print(root.winfo_screenwidth())
    app.mainloop()
