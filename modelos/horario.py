class Horario:
    """Clase que representa el horario de un grupo académico (Composición)."""

    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.salon = salon

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El día debe ser un texto no vacío.")
        self.__dia = valor

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La hora de inicio debe ser un texto no vacío.")
        self.__hora_inicio = valor

    @property
    def hora_fin(self):
        return self.__hora_fin

    @hora_fin.setter
    def hora_fin(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La hora de fin debe ser un texto no vacío.")
        self.__hora_fin = valor

    @property
    def salon(self):
        return self.__salon

    @salon.setter
    def salon(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El salón debe ser un texto no vacío.")
        self.__salon = valor

    def mostrar_horario(self):
        print(f"📅 Horario: {self.dia} de {self.hora_inicio} a {self.hora_fin} en el salón {self.salon}")