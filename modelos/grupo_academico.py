from modelos.horario import Horario
from modelos.asignatura import Asignatura
from modelos.docente import Docente
from modelos.estudiante import Estudiante
from modelos.excepciones import EstudianteDuplicadoError, CapacidadMaximaError, EstudianteNoMatriculadoError

class GrupoAcademico:
    """Clase que representa un grupo académico (Fases 2 y 3)."""

    def __init__(self, codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon):
        self.codigo = codigo
        self.asignatura = asignatura
        self.docente = docente
        self.capacidad_maxima = capacidad_maxima
        
        # COMPOSICIÓN: El grupo crea su propio horario por dentro
        self.horario = Horario(dia, hora_inicio, hora_fin, salon)
        
        # Encapsulamiento: Lista privada
        self.__estudiantes_matriculados = []

    # --- VALIDACIONES CON SETTERS ---
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El código del grupo debe ser un texto no vacío.")
        self.__codigo = valor

    @property
    def asignatura(self):
        return self.__asignatura

    @asignatura.setter
    def asignatura(self, valor):
        if not isinstance(valor, Asignatura):
            raise ValueError("La asignatura debe ser un objeto de tipo Asignatura.")
        self.__asignatura = valor

    @property
    def docente(self):
        return self.__docente

    @docente.setter
    def docente(self, valor):
        if not isinstance(valor, Docente):
            raise ValueError("El docente debe ser un objeto de tipo Docente.")
        self.__docente = valor

    @property
    def capacidad_maxima(self):
        return self.__capacidad_maxima

    @capacidad_maxima.setter
    def capacidad_maxima(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
            raise ValueError("La capacidad máxima debe ser un número entero mayor a cero.")
        self.__capacidad_maxima = valor

    # --- MÉTODOS ---
    def mostrar_informacion_grupo(self):
        print(f"--- GRUPO {self.codigo} ---")
        print(f"Asignatura: {self.asignatura.nombre} | Docente: {self.docente.nombre}")
        print(f"Capacidad: {self.capacidad_maxima} | Matriculados: {len(self.__estudiantes_matriculados)}")
        self.horario.mostrar_horario()

    def matricular_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise ValueError("Solo se pueden matricular objetos de tipo Estudiante.")
        
        # Comparar por código estudiantil, no por objeto
        for est in self.__estudiantes_matriculados:
            if est.codigo_estudiantil == estudiante.codigo_estudiantil:
                raise EstudianteDuplicadoError(f"El estudiante con código {estudiante.codigo_estudiantil} ya está matriculado en este grupo.")
        
        if len(self.__estudiantes_matriculados) >= self.capacidad_maxima:
            raise CapacidadMaximaError(f"El grupo {self.codigo} ya alcanzó su capacidad máxima de {self.capacidad_maxima} estudiantes.")
        
        self.__estudiantes_matriculados.append(estudiante)
        print(f"✅ Estudiante {estudiante.nombre} matriculado en el grupo {self.codigo}.")

    def retirar_estudiante(self, codigo_estudiantil):
        for est in self.__estudiantes_matriculados:
            if est.codigo_estudiantil == codigo_estudiantil:
                self.__estudiantes_matriculados.remove(est)
                print(f"✅ Estudiante {est.nombre} retirado del grupo {self.codigo}.")
                return
        raise EstudianteNoMatriculadoError(f"El estudiante con código {codigo_estudiantil} no está matriculado en este grupo.")

    def mostrar_estudiantes(self):
        print(f"Estudiantes matriculados en el grupo {self.codigo}:")
        for est in self.__estudiantes_matriculados:
            print(f"- {est.nombre} ({est.codigo_estudiantil})")