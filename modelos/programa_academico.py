class ProgramaAcademico:
    """Clase que representa un programa académico de la universidad."""

    def __init__(self, codigo, nombre, facultad, num_semestres):
        self.codigo = codigo
        self.nombre = nombre
        self.facultad = facultad
        self.num_semestres = num_semestres

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
            raise ValueError("El nombre del programa debe ser un texto no vacío.")
        self.__nombre = valor

    @property
    def facultad(self):
        return self.__facultad

    @facultad.setter
    def facultad(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La facultad debe ser un texto no vacío.")
        self.__facultad = valor

    @property
    def num_semestres(self):
        return self.__num_semestres

    @num_semestres.setter
    def num_semestres(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("El número de semestres debe ser un número entero.")
        if valor <= 0:
            raise ValueError("El número de semestres debe ser mayor a cero.")
        self.__num_semestres = valor
        
    def mostrar_informacion(self):
        """Imprime los datos del programa académico en consola."""
        print(f"Programa: {self.nombre} | Código: {self.codigo} | Facultad: {self.facultad} | Semestres: {self.num_semestres}")