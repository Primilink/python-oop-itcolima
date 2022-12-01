import tkinter as tk
import tkinter.messagebox as mb


class ContactosForm(tk.LabelFrame):
    campos = ('Last Name', 'First Name', 'Phone', 'Email')

    def __init__(self, master, **kwargs):
        super().__init__(master, text='Contacts', padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.entries = list(map(self.create_campo, enumerate(self.campos)))

    def create_campo(self, campo):
        position, text = campo
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame)
        label.grid(row=position, column=0, pady=10)
        entry.grid(row=position, column=1, pady=10)
        return entry


class ContactoNuevo(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.form = ContactosForm(self)
        self.form.pack(padx=10, pady=10)

    def show(self):
        self.grab_set()
        self.wait_window()


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
