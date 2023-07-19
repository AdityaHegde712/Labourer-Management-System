from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import os, sys
import config as c
import worker

title = "Worker Contact Details"
title_font = ('Times 24')
label_font = ('Arial 12')

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        global py_version
        py_version = sys.version_info[0]
        self.display()

    def add_widgets(self):
        def open_file():
            root.destroy()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "Home.png")
        image = Image.open(image_path)
        image = image.resize((50, 50))  # Resize the image as needed
        photo = ImageTk.PhotoImage(image)

        self.button = Button(self.master, image=photo, command=open_file)
        self.button.image = photo  # Store a reference to the image to prevent garbage collection
        self.button.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

        # Labels
        # self.l1 = Label(self.master, anchor="center", text=title, font=title_font).place(relx=0.4, rely=0.1)
        self.l1 = Label(self.master, anchor="center", text=title, font=title_font).grid(row=0, column=1, columnspan=1)

        # Treeview
        self.treeview = Treeview(self.master, columns=("0", "1"), show="headings")
        self.treeview.grid(row=1, column=1, columnspan=1)

        # Define column headings
        self.treeview.heading("0", text="Name")
        self.treeview.heading("1", text="Number")

        total_amount = 0  # Variable to store the total amount
        for data in worker.select_all():
            self.treeview.insert("", "end", values=(data['name'], data['phone_no']))

    # 4 columns, 9 rows
    def setup_window(self, root):
        Grid.rowconfigure(root, index=0, weight=1)
        Grid.rowconfigure(root, index=1, weight=1)
        Grid.rowconfigure(root, index=2, weight=1)
        Grid.rowconfigure(root, index=3, weight=1)
        Grid.rowconfigure(root, index=4, weight=1)
        Grid.rowconfigure(root, index=5, weight=1)
        Grid.rowconfigure(root, index=6, weight=1)
        Grid.rowconfigure(root, index=7, weight=1)
        Grid.rowconfigure(root, index=8, weight=1)
        Grid.columnconfigure(root, index=0, weight=1)
        Grid.columnconfigure(root, index=1, weight=1)
        Grid.columnconfigure(root, index=2, weight=1)
        Grid.columnconfigure(root, index=3, weight=1)
        root.columnconfigure(0, minsize=20)
        root.columnconfigure(3, minsize=20)

    def display(self):
        self.winfo_toplevel().title("Labourer Management System")
        self.setup_window(root)
        self.add_widgets()


if __name__ == "__main__":
    root = Tk()
    root.geometry("700x400")
    app = Application(master=root)
    app.mainloop()
