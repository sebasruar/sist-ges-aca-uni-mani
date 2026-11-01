from modelos.persona import Persona
from modelos.programa_academico import ProgramaAcademico
from modelos.asignatura import Asignatura
from modelos.estudiante import Estudiante
from modelos.docente import Docente
from modelos.administrativo import Administrativo
from modelos.grupo_academico import GrupoAcademico
from modelos.sistema_academico import SistemaAcademico
from modelos.excepciones import (
    EstudianteDuplicadoError, 
    CapacidadMaximaError, 
    EstudianteNoMatriculadoError, 
    AsignaturaNoEncontradaError, 
    ProgramaNoEncontradoError
)

if __name__ == "__main__":
    print("--- 1. VERIFICAR QUE NO SE PUEDE CREAR UNA PERSONA DIRECTAMENTE ---")
    try:
        p = Persona("123", "Falso", "falso@umanizales.edu.co")
        print("❌ ERROR: ¡Se pudo crear una Persona! La clase no es abstracta.")
    except TypeError as e:
        print(f"✅ Correcto. Error capturado (Persona es abstracta): {e}")

    print("\n--- 2. CREACIÓN DE PROGRAMAS, ASIGNATURAS, DOCENTES Y ESTUDIANTES ---")
    prog_ingenieria = ProgramaAcademico("ING01", "Ingeniería de Sistemas", "Facultad de Ingenierías", 10)
    prog_medicina = ProgramaAcademico("MED01", "Medicina", "Facultad de Salud", 12)

    asig_prog = Asignatura("PRG1", "Programación I", 4, prog_ingenieria)
    asig_anatomia = Asignatura("ANA1", "Anatomía", 6, prog_medicina)

    doc1 = Docente("202", "Ana María", "ana@umanizales.edu.co", "DOC001", "Ingenierías", "Planta", 20)
    
    est1 = Estudiante("101", "Sebastián", "sebas@umanizales.edu.co", "EST001", prog_ingenieria, 3, 4.5)
    est2 = Estudiante("102", "Valentina", "valen@umanizales.edu.co", "EST002", prog_medicina, 5, 4.8)
    est3 = Estudiante("103", "Andrés", "andres@umanizales.edu.co", "EST003", prog_ingenieria, 2, 3.9)

    print("Programas, asignaturas, docentes y estudiantes creados con éxito.")

    print("\n--- 3. CREACIÓN DE HORARIOS Y AL MENOS DOS GRUPOS ACADÉMICOS ---")
    # El constructor de GrupoAcademico ahora pide los datos del horario directamente
    grupo1 = GrupoAcademico("G01", asig_prog, doc1, 2, "Lunes", "08:00", "10:00", "Aula 201")
    grupo2 = GrupoAcademico("G02", asig_anatomia, doc1, 2, "Martes", "14:00", "16:00", "Aula 305")

    print("Grupos académicos creados.")

    print("\n--- 4. MATRÍCULA CORRECTA DE ESTUDIANTES ---")
    try:
        grupo1.matricular_estudiante(est1)
        grupo1.matricular_estudiante(est2)
    except (EstudianteDuplicadoError, CapacidadMaximaError) as e:
        print(f"Error inesperado en matrícula: {e}")

    print("\n--- 5. INTENTO DE MATRICULAR UN ESTUDIANTE DUPLICADO ---")
    try:
        grupo1.matricular_estudiante(est1)
    except EstudianteDuplicadoError as e:
        print(f"Error capturado (Estudiante duplicado): {e}")

    print("\n--- 6. INTENTO DE SUPERAR LA CAPACIDAD DE UN GRUPO ---")
    try:
        grupo1.matricular_estudiante(est3)
    except CapacidadMaximaError as e:
        print(f"Error capturado (Capacidad máxima): {e}")

    print("\n--- 7. RETIRO CORRECTO DE UN ESTUDIANTE ---")
    try:
        grupo1.retirar_estudiante("EST001")
    except EstudianteNoMatriculadoError as e:
        print(f"Error inesperado: {e}")

    print("\n--- 8. INTENTO DE RETIRAR UN ESTUDIANTE INEXISTENTE ---")
    try:
        grupo1.retirar_estudiante("EST999")
    except EstudianteNoMatriculadoError as e:
        print(f"Error capturado (Estudiante no matriculado): {e}")

    print("\n--- 9 y 10. BÚSQUEDA DE ASIGNATURA Y PROGRAMA INEXISTENTES ---")
    # Usamos la clase SistemaAcademico para lanzar las excepciones desde ahí
    sistema = SistemaAcademico()
    sistema.agregar_programa(prog_ingenieria)
    sistema.agregar_programa(prog_medicina)
    sistema.agregar_asignatura(asig_prog)
    sistema.agregar_asignatura(asig_anatomia)

    try:
        sistema.buscar_asignatura("INEXISTENTE")
    except AsignaturaNoEncontradaError as e:
        print(f"Error capturado (Asignatura no encontrada): {e}")

    try:
        sistema.buscar_programa("INEXISTENTE")
    except ProgramaNoEncontradoError as e:
        print(f"Error capturado (Programa no encontrado): {e}")

    print("\n--- 11. CONTINUIDAD DEL PROGRAMA ---")
    print("El programa continúa ejecutándose después de controlar cada excepción.")

    print("\n--- 12. POLIMORFISMO: LISTA HETEROGÉNEA CON UN SOLO CICLO (AC1) ---")
    
    # Creamos 2 docentes y 2 administrativos adicionales para tener 6 personas
    doc2 = Docente("203", "Carlos", "carlos@umanizales.edu.co", "DOC002", "Salud", "Cátedra", 10)
    
    adm1 = Administrativo("303", "Luis", "luis@umanizales.edu.co", "ADM001", "Registro", "Coordinador", "Diurna")
    adm2 = Administrativo("304", "Marta", "marta@umanizales.edu.co", "ADM002", "Biblioteca", "Auxiliar", "Nocturna")

    # Lista heterogénea con 6 personas (2 est, 2 doc, 2 adm)
    comunidad = [est1, est2, doc1, doc2, adm1, adm2]

    # Un solo ciclo for, sin if ni isinstance
    for persona in comunidad:
        persona.mostrar_informacion()
        persona.realizar_actividad_principal()
        print("-" * 40)

    print("\n--- INFORMACIÓN DE LOS GRUPOS ---")
    grupo1.mostrar_informacion_grupo()
    grupo1.mostrar_estudiantes()
    grupo2.mostrar_informacion_grupo()