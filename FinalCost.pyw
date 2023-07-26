from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import os, sys
import config as c
import attendance as a
import attendanceHelperFunctionsForFrontEnd as aHelper
import dailyEntries as de
import dailyEntriesHelperFunctionsForFrontEnd as deHelper
from translate import Translator

title = "Total Daily Worker Wages"
title_font = ('Times 24')
label_font = ('Arial 12')

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.date_range = sys.argv[1:]
        print("Received date range: ", self.date_range)
        self.total_daily_cost = IntVar()
        self.total_monthly_cost = IntVar()
        self.display()

    def get_costs(self): # Retrieve the values from the database here
        daily_entries = de.select_by_date_and_task(date_range=self.date_range, sort_by_date=True)
        monthly_entries = a.select_by_params(date=self.date_range, sort_by_date=True)
        self.total_daily_cost = deHelper.calculate_wage_by_phone_no(entries=daily_entries)
        self.total_monthly_cost = aHelper.calculate_wage(list_of_entries=monthly_entries)
        print(f"Total Daily Cost = {self.total_daily_cost} \nTotal Monthly Cost = {self.total_monthly_cost}")


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
        self.l1 = Label(self.master, anchor="center", text=title, font=title_font).grid(row=0, column=1, columnspan=1)

        # Treeview
        self.treeview = Treeview(self.master, columns=("0", "1"), show="headings")
        self.treeview.grid(row=1, column=1, columnspan=1)

        # Define column headings
        self.treeview.heading("0", text="Type")
        self.treeview.heading("1", text="Money")

        # Add sample data to the treeview
        self.get_costs()
        sample_data = [
            ("Total (Daily Workers)", self.total_daily_cost),
            ("Total (Monthly Workers)", self.total_monthly_cost),
            ("Grand Total", (self.total_daily_cost + self.total_monthly_cost))
        ]

        for data in sample_data:
            self.treeview.insert("", "end", values=data)

        self.btn7 = Button(self.master, text="Telugu", command=self.translate_to_telugu, width=15)
        self.btn7.place(relx=0.87, rely=0.85)
        self.btn8 = Button(self.master, text="Kannada", command=self.translate_to_kannada, width=15)
        self.btn8.place(relx=0.87, rely=0.92)

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
    app = Application(master=root)
    app.mainloop()
