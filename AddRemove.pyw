import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import os
import config as c
import worker as w
from translate import Translator

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def clear_fields(self):
        # Clear the entry fields
        self.eFName.delete(0, tk.END)
        self.eLName.delete(0, tk.END)
        self.ePNo.delete(0, tk.END)

    def create_widgets(self):
        self.master.title("Labourer Management System")
        self.page_title = Label(self.master, anchor="center", text="Add/Remove Worker", font=("Arial", 20, "bold"))
        self.page_title.place(relx=0.5, rely=0.1, anchor="center")

        def send_details(flag):
            entry = {
                "phone_no": str(self.ePNo.get()),
                "name": (str(self.eFName.get()) + ' ' + str(self.eLName.get()))
            }
            if flag == 1:
                w.insert_one(entry)
            else:
                w.delete_one_by_phone_no(entry["phone_no"])  # TO BE MODIFIED IN THE BACKEND, DO NOT USE DELETE WORKER FOR NOW
            self.clear_fields()

        def open_file():
            root.destroy()

        self.l1 = Label(self.master, anchor="w", text="First Name", font=10)
        self.l2 = Label(self.master, anchor="w", text="Last Name", font=10)
        self.l3 = Label(self.master, anchor="w", text="Phone Number", font=10)

        self.l1.place(relx=0.3, rely=0.3)
        self.l2.place(relx=0.3, rely=0.4)
        self.l3.place(relx=0.3, rely=0.5)

        self.eFName = Entry(self.master, width=40)
        self.eLName = Entry(self.master, width=40)
        self.ePNo = Entry(self.master, width=40)

        self.eFName.place(relx=0.51, rely=0.3)
        self.eLName.place(relx=0.51, rely=0.4)
        self.ePNo.place(relx=0.51, rely=0.5)

        self.style = Style()
        self.style.configure('D.TButton', foreground='black', background='white')

        self.btn = Button(self.master, text="Add Worker", style="D.TButton", 
                          command=lambda: send_details(1), width=17)
        self.btn.place(relx=0.45, rely=0.6)

        self.btn = Button(self.master, text="Remove Worker", style="D.TButton", 
                          command=lambda: send_details(2), width=17)
        self.btn.place(relx=0.45, rely=0.65)


        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "Home.png")
        image = Image.open(image_path)
        image = image.resize((50, 50))  # Resize the image as needed
        photo = ImageTk.PhotoImage(image)

        self.button = Button(self.master, image=photo, command=open_file)
        self.button.image = photo  # Store a reference to the image to prevent garbage collection
        self.button.place(relx=0.04, rely=0.07, anchor="center")

        self.btn7 = Button(self.master, text="Telugu", command=self.translate_to_telugu, width=15)
        self.btn7.place(relx=0.87, rely=0.85)
        self.btn8 = Button(self.master, text="Kannada", command=self.translate_to_kannada, width=15)
        self.btn8.place(relx=0.87, rely=0.92)
    
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
    root = tk.Tk()
    root.geometry("900x500")

    app = Application(master=root)

    app.mainloop()
