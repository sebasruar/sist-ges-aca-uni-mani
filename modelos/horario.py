class Horario:
    """Clase que representa el horario de un grupo académico (Composición)."""

    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.salon = salon

    def mostrar_horario(self):
        print(f"📅 Horario: {self.dia} de {self.hora_inicio} a {self.hora_fin} en el salón {self.salon}")