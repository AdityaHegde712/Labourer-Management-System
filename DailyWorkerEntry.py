from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image
import os
import sys
import dailyEntries as de
import tasks as t

root = Tk()
root.geometry("1340x750")

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        global py_version
        py_version = sys.version_info[0]
        self.Task_Name = StringVar()
        self.Task_Name.set("Task Name")
        self.create_widgets()

    def open_file(self):
        root.destroy()

    def refresh_page(self):
        # Perform any necessary actions with the stored details
        entry = {
            "name": str(self.eName.get()),
            "phone_no": str(self.eNo.get()),
            "task": str(self.Task_Name.get()),
            "wage": int(self.eWage.get()),
            "date": str(self.date_picker.get_date())
        }
        de.insert_one(entry)

        # Clear the entry fields
        self.eName.delete(0, END)
        self.eNo.delete(0, END)
        self.eWage.delete(0, END)

    def get_selected_date(self):
        selected_date = self.date_picker.get_date()
        print(f"Selected Date: {selected_date}")

    def create_widgets(self):
        self.master.title("Daily Worker Entry")

        self.page_title = Label(self.master, anchor="center", text="Daily Worker Entry", font=("Arial", 20, "bold"))
        self.page_title.grid(row=0, column=2, sticky="N", pady=10)

        Grid.rowconfigure(self.master, index=0, weight=1)
        Grid.columnconfigure(self.master, index=0, weight=1)
        Grid.rowconfigure(self.master, index=1, weight=1)
        Grid.columnconfigure(self.master, index=1, weight=1)
        Grid.rowconfigure(self.master, index=2, weight=1)
        Grid.columnconfigure(self.master, index=2, weight=1)
        Grid.rowconfigure(self.master, index=3, weight=1)
        Grid.columnconfigure(self.master, index=3, weight=1)
        Grid.rowconfigure(self.master, index=4, weight=1)
        Grid.columnconfigure(self.master, index=4, weight=1)
        Grid.rowconfigure(self.master, index=5, weight=1)
        Grid.columnconfigure(self.master, index=5, weight=1)

        self.l1 = Label(self.master, anchor="center", text="Name", font=10)
        self.l2 = Label(self.master, anchor="center", text="Phone Number", font=10)
        self.l3 = Label(self.master, anchor="center", text="Work Done", font=10)
        self.l5 = Label(self.master, anchor="center", text="Wage", font=10)
        self.l1.grid(row=0)
        self.l2.grid(row=1)
        self.l3.grid(row=2)
        self.l5.grid(row=4)

        self.eName = Entry(self.master, width=40)
        self.eNo = Entry(self.master, width=40)
        self.eWage = Entry(self.master, width=40)

        self.eName.grid(row=0, column=1, sticky=W)
        self.eNo.grid(row=1, column=1, sticky=W)
        self.eWage.grid(row=4, column=1, sticky=W)

        tasks = t.fetch_all()
        for task in tasks:
            tasks[tasks.index(task)] = task[0]
        drop = ttk.Combobox(self.master, textvariable=self.Task_Name, values=tasks, state="readonly", font=10)
        drop.grid(row=2, column=1, sticky=W)

        self.style = ttk.Style()
        self.style.configure("TButton", foreground="black", background="white", padding=6)

        self.btn = ttk.Button(self.master, text="Register Entry", command=self.refresh_page, style="TButton")
        self.btn.grid(row=4, column=3, sticky="SEW")

        # Date Picker
        self.master.title("Date Picker")

        self.date_picker = DateEntry(self.master, width=16, background="dark grey",
                                     foreground="white", borderwidth=2)
        self.date_picker.grid(row=3, column=0, padx=10, pady=10)

        self.date_btn = ttk.Button(self.master, text="Select Date", command=self.get_selected_date, style="TButton")
        self.date_btn.grid(row=3, column=1, padx=10, pady=10)

        # Load the image
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "Home.png")
        image = Image.open(image_path)
        image = image.resize((50, 50))  # Resize the image as needed
        photo = ImageTk.PhotoImage(image)

        # Create a button with the image
        self.button = Button(self.master, image=photo, command=self.open_file)
        self.button.image = photo  # Store a reference to the image to prevent garbage collection
        self.button.place(relx=0.04, rely=0.04, anchor=CENTER)


app = Application(master=root)
app.mainloop()
