from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image
import os
import sys
import dailyEntries as de
import tasks as t
from translate import Translator

root = Tk()
root.geometry("900x500")

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
        self.page_title.grid(row=0, column=2, sticky="N", pady=10, columnspan=2)

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
        Grid.rowconfigure(self.master, index=6, weight=1)
        Grid.rowconfigure(self.master, index=7, weight=1)
        Grid.rowconfigure(self.master, index=8, weight=1)
        Grid.rowconfigure(self.master, index=9, weight=1)
        Grid.rowconfigure(self.master, index=10, weight=1)
        Grid.rowconfigure(self.master, index=11, weight=1)
        Grid.rowconfigure(self.master, index=12, weight=1)

        self.l1 = Label(self.master, anchor="center", text="Name:", font=10)
        self.l2 = Label(self.master, anchor="center", text="Phone Number:", font=10)
        self.l3 = Label(self.master, anchor="center", text="Work Done:", font=10)
        self.l5 = Label(self.master, anchor="center", text="Wage:", font=10)
        self.l6 = Label(self.master, anchor="center", text="Date:", font=10)

        self.l1.grid(row=2, column=1, sticky=E)
        self.l2.grid(row=4, column=1, sticky=E)
        self.l3.grid(row=6, column=1, sticky=E)
        self.l5.grid(row=8, column=1, sticky=E)
        self.l6.grid(row=10, column=1, sticky=E)

        self.eName = Entry(self.master, width=20, font=10)
        self.eNo = Entry(self.master, width=20, font=10)
        self.eWage = Entry(self.master, width=20, font=10)

        self.eName.grid(row=2, column=2, padx=15, sticky=W)
        self.eNo.grid(row=4, column=2, padx=15, sticky=W)
        self.eWage.grid(row=8, column=2, padx=15, sticky=W)

        tasks = t.fetch_all()
        for task in tasks:
            tasks[tasks.index(task)] = task[0]
        drop = ttk.Combobox(self.master, textvariable=self.Task_Name, values=tasks, state="readonly", width=18, font=10)
        drop.grid(row=6, column=2, sticky=W, padx=15)


        self.btn = ttk.Button(self.master, text="Register Entry", command=self.refresh_page, width=20)
        self.btn.grid(row=12, column=5, sticky="SE", padx=20, pady=20)

        # Date Picker
        self.master.title("Labourer Management System")

        self.date_picker = DateEntry(self.master, width=9, background="dark grey",
                                     foreground="white", borderwidth=2, font=10)
        self.date_picker.grid(row=10, column=2, sticky=W, padx=15)

        self.date_btn = ttk.Button(self.master, text="Select Date", command=self.get_selected_date, style="TButton")
        self.date_btn.grid(row=11, column=2, sticky=W, padx=35)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "Home.png")
        image = Image.open(image_path)
        image = image.resize((50, 50))  # Resize the image as needed
        photo = ImageTk.PhotoImage(image)

        self.button = Button(self.master, image=photo, command=self.open_file)
        self.button.image = photo  # Store a reference to the image to prevent garbage collection
        self.button.grid(row=0, column=0, padx=3, pady=3)

        self.btn7 = Button(self.master, text="Telugu", command=self.translate_to_telugu, width=15)
        self.btn7.place(relx=0.84, rely=0.75)
        self.btn8 = Button(self.master, text="Kannada", command=self.translate_to_kannada, width=15)
        self.btn8.place(relx=0.84, rely=0.82)
    
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


app = Application(master=root)
app.mainloop()
