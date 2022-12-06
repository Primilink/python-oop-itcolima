import sqlite3
from contactos_view import ContactosView
from contactos_controller import ContactosController
from contactos_repository import ContactsRepository


def main():
    with sqlite3.connect('contactos.db') as conn:
        print('Conectado a la base de datos')
        c = conn.cursor()
        c.execute(
            ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='contacts' ''')

        # print result
        if c.fetchone()[0] == 1:
            print('Table exists.')
            repo = ContactsRepository(conn)
            view = ContactosView()
            controller = ContactosController(repo, view)
            view.set_controller(controller)
            controller.start()
        else:
            print('Table does not exist.')
            c.execute('''CREATE TABLE contacts (
                last_name text,
                first_name text,
                phone text,
                email text
            )''')


if __name__ == "__main__":
    main()
