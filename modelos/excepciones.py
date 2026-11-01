class EstudianteDuplicadoError(Exception):
    """Se lanza cuando el estudiante ya está matriculado en el grupo."""
    pass

class CapacidadMaximaError(Exception):
    """Se lanza cuando el grupo alcanzó su capacidad máxima."""
    pass

class EstudianteNoMatriculadoError(Exception):
    """Se lanza cuando se intenta retirar un estudiante que no está en el grupo."""
    pass

class AsignaturaNoEncontradaError(Exception):
    """Se lanza cuando la asignatura buscada no existe."""
    pass

class ProgramaNoEncontradoError(Exception):
    """Se lanza cuando el programa académico buscado no existe."""
    pass