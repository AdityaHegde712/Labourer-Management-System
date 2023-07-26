from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import tasks
import os
import sys
from translate import Translator

title = "Add or Remove Regular Tasks"
title_font = ('Times 24')
label_font = ('Arial 16')
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

        self.task_entry = Entry(self.master, width=15, font=16)
        self.task_entry.grid(row=2, column=2, sticky=W)
        self.b1 = Button(self.master, text=add_task, command=lambda: self.process_tasks(0)).grid(row=4, column=1, sticky=NE, padx=10)
        self.b2 = Button(self.master, text=remove_task, command=lambda: self.process_tasks(1)).grid(row=4, column=2, sticky=NW, padx=10)
        self.btn7 = Button(self.master, text="Telugu", command=self.translate_to_telugu, width=15)
        self.btn7.place(relx=0.87, rely=0.85)
        self.btn8 = Button(self.master, text="Kannada", command=self.translate_to_kannada, width=15)
        self.btn8.place(relx=0.87, rely=0.92)

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
