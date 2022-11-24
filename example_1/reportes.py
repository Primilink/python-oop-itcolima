class Reporte():
    def __init__(self, listaEmpleados):
        self._listaEmpleados = listaEmpleados

    def printReporte():
        pass


class ReporteTotal(Reporte):
    def printReporte(self):
        print("---Reporte TOTAL---")
        print("-------------------")
        for empleado in self._listaEmpleados:
            print(
                f'{empleado.getNombreCompleto()}, {empleado.salario}, {empleado.puesto}, {empleado.programacion}')


class ReporteContabilidad(Reporte):
    def printReporte(self):
        print("---Reporte de contabilidad---")
        print("-----------------------------")
        total_salarios = 0
        for empleado in self._listaEmpleados:
            print(f'{empleado.getNombreCompleto()}, {empleado.salario}')
            total_salarios += empleado.salario
        print(f'//Total de salarios: {total_salarios}')


class ReporteEmpleados(Reporte):
    def printReporte(self):
        print("--- Reporte de empleados ----")
        print("-----------------------------")
        for empleado in self._listaEmpleados:
            print(f'{empleado.getNombreCompleto()}, {empleado.puesto}')


class ReporteProgramacion(Reporte):
    def printReporte(self):
        print("--- Reporte de programacion ----")
        print("--------------------------------")
        for empleado in self._listaEmpleados:
            print(f'{empleado.getNombreCompleto()}, {empleado.programacion}')
