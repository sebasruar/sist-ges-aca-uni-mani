from modelos.persona import Persona
from modelos.programa_academico import ProgramaAcademico
from modelos.asignatura import Asignatura

if __name__ == "__main__":
    print("--- FASE 1 Y 2: Clases base y validaciones ---")
    prog_ingenieria = ProgramaAcademico("ING01", "Ingeniería de Sistemas", "Facultad de Ingenierías", 10)
    asig_prog = Asignatura("PRG1", "Programación I", 4, prog_ingenieria)
    mi_persona = Persona("12345", "Sebastián", "sebas@umanizales.edu.co")

    mi_persona.mostrar_informacion()
    prog_ingenieria.mostrar_informacion()
    asig_prog.mostrar_informacion()

    print("\n--- PRUEBAS DE VALIDACIÓN ---")
    try:
        mi_persona.correo = "   "
    except ValueError as e:
        print(f"Error capturado: {e}")