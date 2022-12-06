from contactos_view import ContactosView, ContactoNuevo


class ContactosController(object):
    def __init__(self, repo, view):
        self.repo = repo
        self.view = view
        self.contacts = list(repo.get_contacts())
        self.selection = None

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

    def select_contact(self, index):
        self.selection = index
        contact = self.contacts[index]
        self.view.load_details(contact)

    def update_contact(self):
        if not self.selection:
            return
        rowid = self.contacts[self.selection].rowid
        update_contact = self.view.get_data()
        update_contact.rowid = rowid

        contact = self.repo.update_contact(update_contact)
        self.contacts[self.selection] = contact
        self.view.update_contact(contact, self.selection)

    def delete_contact(self):
        if not self.selection:
            return

        contact = self.contacts[self.selection]
        self.repo.delete_contact(contact)
        self.view.delete_contact(self.selection)
