from empleado import Gerente
from empleado import Tecnico
from empleado import Gestor
from empleado import Administrador
from reportes import ReporteTotal
from reportes import ReporteContabilidad
from reportes import ReporteEmpleados
from reportes import ReporteProgramacion
from programacion import Matutino
from programacion import Vespertino


def main():
    lista_empleados = []
    lista_empleados.append(Gerente("Juan", "Pérez", 10000, Matutino()))
    lista_empleados.append(Tecnico("Pedro", "Gtz", 5000, Vespertino()))
    lista_empleados.append(Gestor("Maria", "Martínez", 4000, Matutino()))
    lista_empleados.append(Administrador("Jose", "Doe", 3000, Vespertino()))

    reportes = [ReporteEmpleados(lista_empleados), ReporteContabilidad(
        lista_empleados), ReporteProgramacion(lista_empleados), ReporteTotal(lista_empleados)]

    for reporte in reportes:
        reporte.printReporte()
        print("")


if __name__ == "__main__":
    main()
