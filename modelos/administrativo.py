from modelos.persona import Persona

class Administrativo(Persona):
    """Clase que representa a un administrativo de la universidad."""

    def __init__(self, identificacion, nombre, correo, numero_empleado, dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.numero_empleado = numero_empleado
        self.dependencia = dependencia
        self.cargo = cargo
        self.jornada = jornada

    @property
    def numero_empleado(self):
        return self.__numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El número de empleado debe ser un texto no vacío.")
        self.__numero_empleado = valor

    @property
    def dependencia(self):
        return self.__dependencia

    @dependencia.setter
    def dependencia(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La dependencia debe ser un texto no vacío.")
        self.__dependencia = valor

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El cargo debe ser un texto no vacío.")
        self.__cargo = valor

    @property
    def jornada(self):
        return self.__jornada

    @jornada.setter
    def jornada(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La jornada debe ser un texto no vacío.")
        self.__jornada = valor

    def mostrar_informacion(self):
        """Imprime los datos generales y los propios del administrativo."""
        print("--- ADMINISTRATIVO ---")
        super().mostrar_informacion()
        print(f"Empleado: {self.numero_empleado} | Dependencia: {self.dependencia} | Cargo: {self.cargo} | Jornada: {self.jornada}")