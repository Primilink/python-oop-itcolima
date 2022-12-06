from contactos_view import ContactosView, ContactoNuevo


class ContactosController(object):
    def __init__(self, repo, view):
        self.repo = repo
        self.view = view
        self.contacts = list(repo.get_contacts())

    def start(self):
        for c in self.contacts:
            self.view.add_contact(c)
        self.view.mainloop()

    def create_contact(self):
        print("Función create_contact")
        nuevo_contacto = ContactoNuevo(self.view).show()
        if nuevo_contacto:
            contact = self.repo.add_contact(nuevo_contacto)
            self.contacts.append(contact)
            self.view.add_contact(contact)

    def update_contact(self):
        print("Función update_contact")

    def delete_contact(self):
        print("Función delete_contact")
