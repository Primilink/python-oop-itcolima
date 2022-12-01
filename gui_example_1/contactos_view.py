import tkinter as tk
import tkinter.messagebox as mb


class ContactosView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contactos")
        self.geometry("500x500")
        self.resizable(0, 0)

        self.button_new = tk.Button(self, text="Nuevo contacto")
        self.button_new.pack(side=tk.BOTTOM, pady=5)

    def set_controller(self, controller):
        self.button_new.config(command=controller.create_contact)
