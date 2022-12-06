import tkinter as tk
import tkinter.messagebox as mb


class ContactosList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.list = tk.Listbox(self, **kwargs)
        bar = tk.Scrollbar(self, command=self.list.yview)

        self.list.config(yscrollcommand=bar.set)
        bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insert(self, contacto, index=tk.END):
        text = '{}, {}'.format(contacto.last_name, contacto.first_name)
        self.list.insert(index, text)


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
        self.button_add = tk.Button(self, text='Agregar Contacto',
                                    command=self.confirm)
        self.button_add.pack()

    def confirm(self):
        print("Are you sure about that?")

    def show(self):
        self.grab_set()
        self.wait_window()


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
        self.update_form.button_delete.config(
            command=controller.delete_contact)
