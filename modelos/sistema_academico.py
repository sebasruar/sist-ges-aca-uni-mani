from modelos.excepciones import AsignaturaNoEncontradaError, ProgramaNoEncontradoError

class SistemaAcademico:
    """Clase que gestiona las búsquedas en el sistema (Fase 4)."""

    def __init__(self):
        self.programas = []
        self.asignaturas = []

    def agregar_programa(self, programa):
        self.programas.append(programa)

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def buscar_programa(self, codigo):
        """Busca un programa por su código y lanza excepción si no existe."""
        for prog in self.programas:
            if prog.codigo == codigo:
                return prog
        raise ProgramaNoEncontradoError(f"El programa con código '{codigo}' no existe en el sistema.")

    def buscar_asignatura(self, codigo):
        """Busca una asignatura por su código y lanza excepción si no existe."""
        for asig in self.asignaturas:
            if asig.codigo == codigo:
                return asig
        raise AsignaturaNoEncontradaError(f"La asignatura con código '{codigo}' no existe en el sistema.")