from contactos import Contacto


class ContactsRepository(object):
    def __init__(self, conn):
        self.conn = conn

    def to_values(self, contacto):
        return contacto.last_name, contacto.first_name, contacto.phone, contacto.email

    def add_contact(self, contacto):
        sql = "INSERT INTO contacts VALUES (?, ?, ?, ?)"
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(sql, self.to_values(contacto))
            contacto.rowid = cursor.lastrowid
        return contacto

    def get_contacts(self):
        sql = "SELECT rowid, * FROM contacts"

        for row in self.conn.execute(sql):
            contact = Contacto(row[1], row[2], row[3], row[4])
            contact.rowid = row[0]
            yield contact

    def update_contact(self, contacto):
        sql = "UPDATE contacts SET last_name = ?, first_name = ?, phone = ?, email = ? WHERE rowid = ?"
        with self.conn:
            self.conn.execute(sql, self.to_values(contacto) + (contacto.rowid,))
            if self.conn.total_changes == 1:
                print("Contacto actualizado")
        return contacto

    def delete_contact(self, contacto):
        sql = "DELETE FROM contacts WHERE rowid = ?"
        with self.conn:
            self.conn.execute(sql, (contacto.rowid,))
