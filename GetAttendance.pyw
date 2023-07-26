'''
Click on attendance for a given date range
Open new window

Drop down at the top of which employee's attendance you want to see
Accordingly, display in treeview (retrieve all records, filter by date and check for name being the same, 
display if both satisfied)

(See if you can make it dynamically change depending on which name is selected, if not possible, you need to 
create 2 new windows, one intermediate, one with treeview)

(idea to make it dynamic, make the treeview a separate function which loads only when a name is selected, 
otherwise generates nothing. When name selected from dropdown and hit the "select name" button from the right 
of the dropdown, get the name using get(), and then call function to implement treeview. So now everytime a new 
name is selected, treeview will reset and accordingly work. I'M BRILLIANT)
'''

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import sys
import os
import worker as w
import attendance as att
from PIL import ImageTk, Image
from translate import Translator


# 6 rows, 5 columns
title = "View Attendance"
select = "Select Worker"
title_font = ('Times 24')

class Application(Frame):
    global py_version
    py_version = sys.version_info[0]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.date_range = sys.argv[1:]  # Retrieve the date_range argument from the command-line
        print(f"Received Date Range: {self.date_range}")
        self.selected_option = StringVar()

        #Treeview Widget
        self.treeview = Treeview(self.master)

        self.display()

    def add_home_button(self):
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

    def get_name(self):
        selected_name = str(self.selected_option.get())
        self.process_entries_by_name_and_date(selected_name, att.select_by_params(date=self.date_range, sort_by_date=True))

    def process_entries_by_name_and_date(self, name, reference_records):
        worker_id_to_name = {worker['id']: worker['name'] for worker in w.select_all()}
        updated_reference_records = []
        for entry in reference_records:
            if worker_id_to_name.get(entry['worker_id']) == name:
                entry['name'] = worker_id_to_name.get(entry['worker_id'])
                del entry['worker_id'], entry['id'], entry['wage']
                updated_reference_records.append(entry)
        reference_records[:] = updated_reference_records
        self.create_tree_view(reference_records)

    def create_tree_view(self, attendance_records):
        # Function to create the TreeView
    
        # Clear any existing TreeView
        if self.master.winfo_exists() and self.treeview.exists(''):
            self.treeview.delete(*self.treeview.get_children())
        
        # Create the TreeView with 2 columns
        self.treeview["columns"] = ("date", "task")
        # self.treeview.column("#0", width=0)  # Hide the default first column
        
        # Define column headings
        self.treeview.heading("date", text="Date")
        self.treeview.heading("task", text="Task")

        # Configure TreeView to span across 2 columns
        self.treeview.column("#0", width=0, stretch=NO)
        self.treeview.column("date", anchor=CENTER)
        self.treeview.column("task", anchor=CENTER)
        self.treeview.grid(row=3, column=1, columnspan=2)
        
        # Populate the TreeView with attendance records
        for record in attendance_records:
            date = record["date"]
            task = record["task"]
            self.treeview.insert("", END, values=(date, task))

        # YOU'RE TRYING TO FIGURE OUT HOW TO ORGANICALLY MAKE IT SPAN ACROSS 2 COLUMNS AND NOT CREATE 2 SUBCOLUMNS    

    def add_buttons(self):
        self.add_home_button()
        all_workers = [entry['name'] for entry in w.select_all()]
        dropdown = Combobox(self.master, textvariable=self.selected_option, values=all_workers, width=18).grid(row=1, column=1, columnspan=2, sticky=N)
        self.b1 = Button(self.master, text="Select Worker", width=18, command=lambda: self.get_name()).grid(row=1, column=1, columnspan=2, sticky=S)
        self.btn7 = Button(self.master, text="Telugu", command=self.translate_to_telugu, width=15)
        self.btn7.place(relx=0.87, rely=0.85)
        self.btn8 = Button(self.master, text="Kannada", command=self.translate_to_kannada, width=15)
        self.btn8.place(relx=0.87, rely=0.92)

    def add_labels(self):
        self.l1 = Label(self.master, text=title, font=title_font, anchor="center").grid(row=0, column=1, columnspan=2)

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
        # root.columnconfigure(3, minsize=20)
        # root.columnconfigure(0, minsize=20)

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
    root = Tk()
    root.geometry("900x500")
    app = Application(master = root)
    print(root.winfo_screenheight())
    print(root.winfo_screenwidth())
    app.mainloop()

