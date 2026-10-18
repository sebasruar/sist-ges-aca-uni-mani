from modelos.persona import Persona

class Docente(Persona):
    """Clase que representa a un docente de la universidad."""

    def __init__(self, identificacion, nombre, correo, numero_empleado, facultad, tipo_contratacion, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.numero_empleado = numero_empleado
        self.facultad = facultad
        self.tipo_contratacion = tipo_contratacion
        self.horas_semanales = horas_semanales

    @property
    def numero_empleado(self):
        return self.__numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El número de empleado debe ser un texto no vacío.")
        self.__numero_empleado = valor

    @property
    def facultad(self):
        return self.__facultad

    @facultad.setter
    def facultad(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La facultad debe ser un texto no vacío.")
        self.__facultad = valor

    @property
    def tipo_contratacion(self):
        return self.__tipo_contratacion

    @tipo_contratacion.setter
    def tipo_contratacion(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El tipo de contratación debe ser un texto no vacío.")
        self.__tipo_contratacion = valor

    @property
    def horas_semanales(self):
        return self.__horas_semanales

    @horas_semanales.setter
    def horas_semanales(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("Las horas semanales deben ser un número entero.")
        if valor <= 0:
            raise ValueError("Las horas semanales deben ser mayores a cero.")
        self.__horas_semanales = valor

    def mostrar_informacion(self):
        """Imprime los datos generales y los propios del docente."""
        print("--- DOCENTE ---")
        super().mostrar_informacion()
        print(f"Empleado: {self.numero_empleado} | Facultad: {self.facultad} | Contrato: {self.tipo_contratacion} | Horas: {self.horas_semanales}")