from modelos.persona import Persona
from modelos.programa_academico import ProgramaAcademico
from modelos.asignatura import Asignatura
from modelos.estudiante import Estudiante
from modelos.docente import Docente
from modelos.administrativo import Administrativo

if __name__ == "__main__":
    print("--- PRUEBAS DE FUNCIONAMIENTO DEL SISTEMA ---")
    
    # 1. Crear objetos válidos
    prog_ingenieria = ProgramaAcademico("ING01", "Ingeniería de Sistemas", "Facultad de Ingenierías", 10)
    asig_prog = Asignatura("PRG1", "Programación I", 4, prog_ingenieria)
    
    est1 = Estudiante("101", "Sebastián", "sebas@umanizales.edu.co", "EST001", prog_ingenieria, 3, 4.5)
    doc1 = Docente("202", "Ana María", "ana@umanizales.edu.co", "DOC001", "Ingenierías", "Planta", 20)
    adm1 = Administrativo("303", "Carlos", "carlos@umanizales.edu.co", "ADM001", "Registro", "Coordinador", "Diurna")

    print("\n--- MOSTRAR INFORMACIÓN (Sobrescritura) ---")
    est1.mostrar_informacion()
    print() 
    doc1.mostrar_informacion()
    print()
    adm1.mostrar_informacion()

    print("\n--- POLIMORFISMO (Un solo ciclo) ---")
    comunidad = [est1, doc1, adm1]
    
    for persona in comunidad:
        persona.mostrar_informacion()
        print("-" * 30) 

    print("\n--- ACTIVIDAD PRINCIPAL (Polimorfismo) ---")
    for persona in comunidad:
        persona.realizar_actividad_principal()
        print("-" * 30)

    print("\n--- VALIDACIONES (Intentos inválidos) ---")
    try:
        est1.promedio = 6.5
    except ValueError as e:
        print(f"Error capturado (Promedio): {e}")

    try:
        doc1.horas_semanales = -5
    except ValueError as e:
        print(f"Error capturado (Horas docente): {e}")