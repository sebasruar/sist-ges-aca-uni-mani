from modelos.programa_academico import ProgramaAcademico

class Asignatura:
    """Clase que representa una asignatura que pertenece a un programa."""

    def __init__(self, codigo, nombre, creditos, programa):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.programa = programa

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El código debe ser un texto no vacío.")
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre de la asignatura debe ser un texto no vacío.")
        self.__nombre = valor

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("Los créditos deben ser un número entero.")
        if valor <= 0:
            raise ValueError("El número de créditos debe ser mayor a cero.")
        self.__creditos = valor

    @property
    def programa(self):
        return self.__programa

    @programa.setter
    def programa(self, valor):
        if not isinstance(valor, ProgramaAcademico):
            raise ValueError("El programa debe ser una instancia de ProgramaAcademico.")
        self.__programa = valor

    def mostrar_informacion(self):
        """Imprime los datos de la asignatura."""
        print(f"Asignatura: {self.nombre} | Código: {self.codigo} | Créditos: {self.creditos} | Programa: {self.programa.nombre}")