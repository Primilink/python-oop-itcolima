import datetime


class Programacion():
    def getProgramacionInfo(self):
        return f'{self._horaEntrada:%H:%M} - {self._horaSalida:%H:%M}'

    def __str__(self) -> str:
        return self.getProgramacionInfo()


class Matutino(Programacion):
    _horaEntrada = datetime.time(8, 0, 0)
    _horaSalida = datetime.time(16, 0, 0)


class Vespertino(Programacion):
    _horaEntrada = datetime.time(12, 0, 0)
    _horaSalida = datetime.time(20, 0, 0)
