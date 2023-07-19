from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import tasks
import os
import sys

title = "Add or Remove Regular Tasks"
title_font = ('Times 24')
label_font = ('Arial 12')
task_name = "Task Name: "
add_task = "Add Task"
remove_task = "Remove Task"

class Application(Frame):
    global py_version
    py_version = sys.version_info[0]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def add_home_button(self):
        # Home Button
        def open_file():
                root.destroy()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "Home.png")
        image = Image.open(image_path)
        image = image.resize((50, 50))  # Resize the image as needed
        photo = ImageTk.PhotoImage(image)
        
        self.button = Button(self.master, image=photo, command=open_file)
        self.button.image = photo  # Store a reference to the image to prevent garbage collection
        self.button.grid(row=0, column=0, sticky=W, padx=15)
    
    def process_tasks(self, flag):
        task = str(self.task_entry.get())
        print(task)
        if flag == 0:
            tasks.insert_one(task)
        if flag == 1:
             tasks.delete_one(task)
        self.task_entry.delete(0, 'end') 

    def add_buttons_entries(self):
        # rows 4, columns 1 and 2
        self.add_home_button()

        self.task_entry = Entry(self.master, width=15)
        self.task_entry.grid(row=2, column=2, sticky=W)
        self.b1 = Button(self.master, text=add_task, command=lambda: self.process_tasks(0)).grid(row=4, column=1, sticky=E, padx=10)
        self.b2 = Button(self.master, text=remove_task, command=lambda: self.process_tasks(1)).grid(row=4, column=2, sticky=W, padx=10)

    def add_labels(self):
        self.l1 = Label(self.master, anchor="center", text=title, font=title_font).grid(row=0, column=1, columnspan=2)
        self.l2 = Label(self.master, anchor="center", text=task_name, font=label_font).grid(row=2, column=1, sticky=E)

    def setup_window(self, root):
        # 4 columns, 8 rows
        Grid.rowconfigure(root, index = 0, weight = 1)
        Grid.rowconfigure(root, index = 1, weight = 1)
        Grid.rowconfigure(root, index = 2, weight = 1)
        Grid.rowconfigure(root, index = 3, weight = 1)
        Grid.rowconfigure(root, index = 4, weight = 1)
        Grid.rowconfigure(root, index = 5, weight = 1)
        Grid.rowconfigure(root, index = 6, weight = 1)
        Grid.rowconfigure(root, index = 7, weight = 1)
        Grid.columnconfigure(root, index = 0, weight = 1)
        Grid.columnconfigure(root, index = 1, weight = 1)
        Grid.columnconfigure(root, index = 2, weight = 1)
        Grid.columnconfigure(root, index = 3, weight = 1)
        root.columnconfigure(3, minsize=20)
        root.columnconfigure(0, minsize=20)

    def create_widgets(self):
        self.setup_window(root)
        self.master.title("Manage Tasks")
        self.add_labels()
        self.add_buttons_entries()
        

if __name__ == "__main__":
    root = Tk()
    root.geometry("800x300")
    app = Application(master = root)
    print(root.winfo_screenheight())
    print(root.winfo_screenwidth())
    app.mainloop()
