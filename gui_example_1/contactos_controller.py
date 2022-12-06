from contactos_view import ContactosView, ContactoNuevo


class ContactosController(object):
    def __init__(self, view):
        self.view = view

    def start(self):
        self.view.mainloop()

    def create_contact(self):
        print("Función create_contact")
        nuevo_contacto = ContactoNuevo(self.view)
        nuevo_contacto.show()

    def update_contact(self):
        print("Función update_contact")

    def delete_contact(self):
        print("Función delete_contact")
