from contactos_view import ContactosView


class ContactosController(object):
    def __init__(self, view):
        self.view = view

    def start(self):
        self.view.mainloop()

    def create_contact(self):
        print("Función create_contact")
