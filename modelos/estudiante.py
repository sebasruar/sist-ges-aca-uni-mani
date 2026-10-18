from modelos.persona import Persona
from modelos.programa_academico import ProgramaAcademico

class Estudiante(Persona):
    """Clase que representa a un estudiante de la universidad."""

    def __init__(self, identificacion, nombre, correo, codigo_estudiantil, programa, semestre, promedio):
        super().__init__(identificacion, nombre, correo)
        self.codigo_estudiantil = codigo_estudiantil
        self.programa = programa
        self.semestre = semestre
        self.promedio = promedio

    @property
    def codigo_estudiantil(self):
        return self.__codigo_estudiantil

    @codigo_estudiantil.setter
    def codigo_estudiantil(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El código estudiantil debe ser un texto no vacío.")
        self.__codigo_estudiantil = valor

    @property
    def programa(self):
        return self.__programa

    @programa.setter
    def programa(self, valor):
        if not isinstance(valor, ProgramaAcademico):
            raise ValueError("El programa debe ser una instancia de ProgramaAcademico.")
        self.__programa = valor

    @property
    def semestre(self):
        return self.__semestre

    @semestre.setter
    def semestre(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("El semestre debe ser un número entero.")
        if valor <= 0:
            raise ValueError("El semestre debe ser mayor a cero.")
        self.__semestre = valor

    @property
    def promedio(self):
        return self.__promedio

    @promedio.setter
    def promedio(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("El promedio debe ser un número.")
        if valor < 0.0 or valor > 5.0:
            raise ValueError("El promedio debe estar entre 0.0 y 5.0.")
        self.__promedio = valor

    def mostrar_informacion(self):
        """Imprime los datos generales y los datos propios del estudiante."""
        print("--- ESTUDIANTE ---")
        super().mostrar_informacion()
        print(f"Código: {self.codigo_estudiantil} | Programa: {self.programa.nombre} | Semestre: {self.semestre} | Promedio: {self.promedio}")

    def realizar_actividad_principal(self):
        """Imprime la actividad principal del estudiante."""
        print(f"El estudiante cursa el programa de {self.programa.nombre} y está en el semestre {self.semestre}.")