## Introducción a los ORM

### Mapeadores Objeto - Relación

-   Automatiza la transferencia de datos almacenados en tablas de bases de datos relacionales en objetos.
-   Mecanismo para actualizar una base de datos usando objetos de aplicación.
-   Permite la construcción de objetos de aplicación basado en consultas a la base de datos.

Un ORM realiza el _mapeo_ entre objetos de aplicación y tablas de bases de datos relacionales.

Por ejemplo: convierte el siguiente objeto a una tabla:

```{.python}
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

```{.sql}
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);
```

### Patrones de diseño en los ORM

Estàn basados en dos principales patrones de diseño:

-   Patrón de diseño _Data Mapper_, mantener la representación en memoria y el almacén de datos persistente separados entre sí y del propio data mapper.
-   Patrón de diseño _Unit of Work_, que se caracteriza por implementar transacciones permitiendo ralizar commits o rollbacks.

### SQLAlchemy

-   ORM de código abierto para Python.
-   Permite trabajar con múltiples bases de datos relacionales como MySQL, PostgreSQL, SQLite, Oracle, etc.
-   Permite mapear objetos de python POPO (Plain Old Python Objects) a tablas de bases de datos relacionales.
-   Soporta

#### Instalación

```{.bash}
pip install sqlalchemy
```

#### Ejemplo de uso

Definición de clase:

```{.python}
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column('title', String(50))
    in_stock = Column('in_stock', Boolean)
    quantity = Column('quantity', Integer)
    price = Column('price', Numeric)
```

Relación uno a muchos:

```{.python}

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    comments = relationship("Comment)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
```

Relación muchos a uno:

```{.python}
class Tire(Base):
    __tablename__ = 'tires'
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship("Car")

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
```

Relación uno a uno:

```{.python}
class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    mobile_phone = relationship("MobilePhone", uselist=False, back_populates="person")

class MobilePhone(Base):
    __tablename__ = 'mobile_phones'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship("Person", back_populates="mobile_phone")
```

Relación muchos a muchos:

```{.python}
# Tabla asociativa
student_course_association = Table('student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    courses = relationship("Course", secondary=student_course_association)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    students = relationship("Student", secondary=student_course_association)
```

### Sessions

-   Las sesiones permite la implementación del patrón de diseño _Unit of Work_.
-   Se utiliza para garantizar que todas las operaciones se realicen en una transacción.
-   Evita el uso de muchas sentencias SQL para realizar una operación.
