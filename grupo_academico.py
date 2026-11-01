from modelos.horario import Horario

class GrupoAcademico:
    """Clase que representa un grupo académico (Fases 2 y 3)."""

    def __init__(self, codigo, asignatura, docente, capacidad_maxima, horario):
        self.codigo = codigo
        self.asignatura = asignatura
        self.docente = docente
        self.capacidad_maxima = capacidad_maxima
        self.horario = horario  # <-- COMPOSICIÓN: el grupo contiene un objeto Horario
        self.estudiantes_matriculados = []

    def mostrar_informacion_grupo(self):
        print(f"--- GRUPO {self.codigo} ---")
        print(f"Asignatura: {self.asignatura.nombre} | Docente: {self.docente.nombre}")
        print(f"Capacidad: {self.capacidad_maxima} | Matriculados: {len(self.estudiantes_matriculados)}")
        self.horario.mostrar_horario()

    def matricular_estudiante(self, estudiante):
        # Aquí luego pondremos las excepciones
        pass

    def retirar_estudiante(self, codigo_estudiantil):
        # Aquí luego pondremos las excepciones
        pass

    def mostrar_estudiantes(self):
        print("Estudiantes matriculados:")
        for est in self.estudiantes_matriculados:
            print(f"- {est.nombre} ({est.codigo_estudiantil})")