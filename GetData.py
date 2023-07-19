from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry
from datetime import timedelta
from PIL import ImageTk, Image
import os, sys
import dailyEntries as de
import config as c
import subprocess

title = "What would you like to see?"
title_font = ('Times 24')
label_font = ('Arial 12')
select_date = "Select Date Range"

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        global py_version
        py_version = sys.version_info[0]
        self.display()
    
    def date_range(self, start, stop):
        c.date_range = []  # Clear the list before populating
        diff = (stop - start).days
        for i in range(diff + 1):
            day = start + timedelta(days=i)
            c.date_range.append(str(day))
        # print(c.date_range)
        # daily_entries = de.select_all(sort_by_date=True)
        # print(daily_entries)
        return c.date_range  # Return the calculated date range


    def callback_daily(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TotalDaily.py")
        date_range = self.date_range(self.date1.get_date(), self.date2.get_date())
        command = ["python", script_path] + list(date_range)
        subprocess.run(command)

    def callback_monthly(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TotalMonthly.py")
        date_range = self.date_range(self.date1.get_date(), self.date2.get_date())
        command = ["python", script_path] + list(date_range)
        subprocess.run(command)
    
    def callback_final(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FinalCost.py")
        date_range = self.date_range(self.date1.get_date(), self.date2.get_date())
        command = ["python", script_path] + list(date_range)
        subprocess.run(command)
    
    def callback_attendance(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "GetAttendance.py")
        date_range = self.date_range(self.date1.get_date(), self.date2.get_date())
        command = ["python", script_path] + list(date_range)
        subprocess.run(command)
    
    def add_widgets(self):
        def open_file():
            root.destroy()

        # The issue is here somehow I am sure. It says Home.png cannot be opened
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "Home.png")
        image = Image.open(image_path)
        image = image.resize((50, 50))  # Resize the image as needed
        photo = ImageTk.PhotoImage(image)

        self.button = Button(self.master, image=photo, command=open_file)
        self.button.image = photo  # Store a reference to the image to prevent garbage collection
        self.button.grid(row=0, column=0, sticky=W, padx=10)
        
        # Labels
        self.l1 = Label(self.master, anchor="center", text=title, font=title_font).grid(row=0, column=1, columnspan=2)
        self.l2 = Label(self.master, anchor="center", text=select_date, font=label_font).grid(row=1, column=1, columnspan=2)

        # Date Picker
        self.date1 = DateEntry(self.master)
        self.date1.grid(row=2, column=1, padx=30)

        self.date2 = DateEntry(self.master)
        self.date2.grid(row=2, column=2, padx=30)

        self.bt = Button(self.master, text='Select Date',
                         command=lambda: self.date_range(self.date1.get_date(), self.date2.get_date()))
        self.bt.grid(row=3, column=1, columnspan=2, sticky=N)

        # Buttons
        self.bt1 = Button(self.master, text="Total Daily-Worker wages", command=self.callback_daily).grid(row=4, column=1, columnspan=2, sticky=S)
        self.bt1 = Button(self.master, text="Total Monthly-Worker wages", command=self.callback_monthly).grid(row=5, column=1, columnspan=2, sticky=S)
        self.bt1 = Button(self.master, text="Final Costs", command=self.callback_final).grid(row=6, column=1, columnspan=2, sticky=S)
        self.bt1 = Button(self.master, text="Check Monthly Worker Attendance", command=self.callback_attendance).grid(row=7, column=1, columnspan=2, sticky=S)

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
    root.geometry("800x300")
    app = Application(master=root)
    print(root.winfo_screenheight())
    print(root.winfo_screenwidth())
    app.mainloop()

