class Persona:
    """Clase base que representa a una persona en la universidad."""
    
    def __init__(self, identificacion, nombre, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La identificación debe ser un texto no vacío.")
        self.__identificacion = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El correo no puede estar vacío y debe ser texto.")
        self.__correo = valor

    def mostrar_informacion(self):
        """Imprime los datos generales de la persona."""
        print(f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}")