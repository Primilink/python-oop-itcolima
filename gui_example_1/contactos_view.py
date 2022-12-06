import tkinter as tk
import tkinter.messagebox as mb
from contactos import Contacto


class ContactosList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.list = tk.Listbox(self, **kwargs)
        bar = tk.Scrollbar(self, command=self.list.yview)

        self.list.config(yscrollcommand=bar.set)
        bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insert(self, contacto, index=tk.END):
        # print(f'{contacto.first_name} {contacto.last_name} {contacto.phone} {contacto.email} {contacto.rowid}')
        text = '{}, {}'.format(contacto.last_name, contacto.first_name)
        self.list.insert(index, text)

    def delete(self, index):
        self.list.delete(index, index)

    def update(self, contacto, index):
        self.delete(index)
        self.insert(contacto, index)

    def double_click(self, callback):
        def handler(_): return callback(self.list.curselection()[0])
        self.list.bind('<Double-Button-1>', handler)


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

    def get_data(self):
        values = [e.get() for e in self.entries]
        #print("Values: ", values)
        try:
            return Contacto(*values)
        except ValueError as e:
            tk.messagebox.showerror('Error', str(e), parent=self)

    def load_details(self, contact):
        values = (contact.last_name, contact.first_name, contact.phone, contact.email)
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, tk.END)


class ContactoNuevo(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.contact = None
        self.form = ContactosForm(self)
        self.form.pack(padx=10, pady=10)
        self.button_add = tk.Button(self, text='Agregar Contacto', command=self.confirm)
        self.button_add.pack()

    def confirm(self):
        print("Are you sure about that?")
        self.contact = self.form.get_data()
        if self.contact:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()

        return self.contact


class ActualizarContactosForm(ContactosForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.button_save = tk.Button(self, text='Guardar')
        self.button_save.config(bg='green', fg='white')
        self.button_save.pack(side=tk.RIGHT, ipadx=5, padx=10, pady=10)

        self.button_delete = tk.Button(self, text='Eliminar')
        self.button_delete.config(bg='red', fg='white')
        self.button_delete.pack(side=tk.RIGHT, ipadx=5, padx=10, pady=10)


class ContactosView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contactos")
        # self.geometry("500x500")
        self.resizable(0, 0)

        self.button_new = tk.Button(self, text="Nuevo contacto")
        self.button_new.pack(side=tk.BOTTOM, pady=5)

        self.list = ContactosList(self, height=20)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)

        self.update_form = ActualizarContactosForm(self)
        self.update_form.pack(side=tk.RIGHT, padx=10, pady=10)

    def set_controller(self, controller):
        self.button_new.config(command=controller.create_contact)

        self.update_form.button_save.config(command=controller.update_contact)
        self.update_form.button_delete.config(command=controller.delete_contact)

        self.list.double_click(controller.select_contact)

    def add_contact(self, contact):
        self.list.insert(contact)

    def update_contact(self, contact, index):
        self.list.update(contact, index)

    def delete_contact(self, index):
        self.update_form.clear()
        self.list.delete(index)

    def get_data(self):
        return self.update_form.get_data()

    def load_details(self, contact):
        self.update_form.load_details(contact)
