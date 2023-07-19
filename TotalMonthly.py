from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import os, sys
import config as c
import attendance as me
import worker as w

title = "Total Daily Worker Wages"
title_font = ('Times 24')
label_font = ('Arial 12')
# date_range_needed = ['2023-06-20', '2023-06-21', '2023-06-22']

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.date_range = sys.argv[1:]  # Retrieve the date_range argument from the command-line
        print(f"Received Date Range: {self.date_range}\n")
        self.display()

    def get_names(self, monthly_entries, worker_names):
        for entry in monthly_entries:
            for worker in worker_names:
                if entry['worker_id'] == worker['id']:
                    entry['name'] = worker['name']
        return monthly_entries

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
        self.l1 = Label(self.master, anchor="center", text=title, font=title_font).place(relx=0.4, rely=0.1)

        # Treeview
        self.treeview = Treeview(self.master, columns=("date", "name", "activity", "wage"), show="headings")
        self.treeview.place(relx=0.17, rely=0.3)

        # Define column headings
        self.treeview.heading("date", text="Date")
        self.treeview.heading("name", text="Name")
        self.treeview.heading("activity", text="Activity")
        self.treeview.heading("wage", text="Wage")


        total_amount = 0  # Variable to store the total amount
        display_entries = self.get_names(me.select_all(sort_by_date=True), w.select_all())

        # print(display_entries, '\n')
        # for data in [entry for entry in c.sample_monthly_entries if entry[0] in self.date_range]:
        #     self.treeview.insert("", "end", values=data)
        #     wage = int(data[-1].replace("$", ""))
        #     total_amount += wage

        # date name activity wage -------------------------------------------------------------------------------------------------------
        print("Processed date range: ", self.date_range, '\n')
        for entry in display_entries:
            if entry['date'] in self.date_range:
                print(entry)
                data = (entry['date'], entry['name'], entry['task'], entry['wage'])
                self.treeview.insert("", "end", values=data)
                wage = int(entry['wage'])
                total_amount += wage

        # Insert the total amount in the last row and last column
        self.treeview.insert("", "end", values=["", "", "", ""], tags=("",))
        self.treeview.insert("", "end", values=["Total", "", "", f"${total_amount}"], tags=("total",))
        self.treeview.tag_configure("total", font=('Arial 12 bold'))

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
    root.geometry("1080x720")
    app = Application(master=root)
    app.mainloop()
