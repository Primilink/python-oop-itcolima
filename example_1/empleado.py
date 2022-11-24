class Empleado():
    def __init__(self, nombre, apellido, salario, programacion) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self.salario = salario
        self.programacion = programacion

    def getNombreCompleto(self):
        return f'{self._nombre} {self._apellido}'


class Gerente(Empleado):
    puesto = "Gerente General"


class Tecnico(Empleado):
    puesto = "Tecnico"


class Gestor(Empleado):
    puesto = "Gestor(a) de cobranza"


class Administrador(Empleado):
    puesto = "Administrador(a) de servicios de cable"
