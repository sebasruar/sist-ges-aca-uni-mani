from modelos.persona import Persona
from modelos.programa_academico import ProgramaAcademico
from modelos.asignatura import Asignatura
from modelos.estudiante import Estudiante
from modelos.docente import Docente
from modelos.administrativo import Administrativo

if __name__ == "__main__":
    print("--- 1. CREACIÓN DE PROGRAMAS Y ASIGNATURAS ---")
    prog_ingenieria = ProgramaAcademico("ING01", "Ingeniería de Sistemas", "Facultad de Ingenierías", 10)
    prog_medicina = ProgramaAcademico("MED01", "Medicina", "Facultad de Salud", 12)
    
    asig_prog = Asignatura("PRG1", "Programación I", 4, prog_ingenieria)
    asig_anatomia = Asignatura("ANA1", "Anatomía", 6, prog_medicina)

    print("\n--- 2. CONSULTA DE INFORMACIÓN DE PROGRAMAS Y ASIGNATURAS ---")
    prog_ingenieria.mostrar_informacion()
    prog_medicina.mostrar_informacion()
    asig_prog.mostrar_informacion()
    asig_anatomia.mostrar_informacion()

    print("\n--- 3. CREACIÓN DE PERSONAS (2 Estudiantes, 2 Docentes, 2 Administrativos) ---")
    est1 = Estudiante("101", "Sebastián", "sebas@umanizales.edu.co", "EST001", prog_ingenieria, 3, 4.5)
    est2 = Estudiante("102", "Valentina", "valen@umanizales.edu.co", "EST002", prog_medicina, 5, 4.8)
    
    doc1 = Docente("202", "Ana María", "ana@umanizales.edu.co", "DOC001", "Ingenierías", "Planta", 20)
    doc2 = Docente("203", "Carlos", "carlos@umanizales.edu.co", "DOC002", "Salud", "Cátedra", 10)
    
    adm1 = Administrativo("303", "Luis", "luis@umanizales.edu.co", "ADM001", "Registro", "Coordinador", "Diurna")
    adm2 = Administrativo("304", "Marta", "marta@umanizales.edu.co", "ADM002", "Biblioteca", "Auxiliar", "Nocturna")

    print("\n--- 4. MODIFICACIONES VÁLIDAS ---")
    est1.promedio = 4.7
    doc1.horas_semanales = 22
    print(f"Promedio de {est1.nombre} actualizado a: {est1.promedio}")
    print(f"Horas de {doc1.nombre} actualizadas a: {doc1.horas_semanales}")

    print("\n--- 5. VALORES INVÁLIDOS (Mínimo 3) ---")
    try:
        est2.promedio = 6.5
    except ValueError as e:
        print(f"Error capturado (Promedio inválido): {e}")

    try:
        doc2.horas_semanales = -5
    except ValueError as e:
        print(f"Error capturado (Horas inválidas): {e}")

    try:
        adm2.correo = "   "
    except ValueError as e:
        print(f"Error capturado (Correo vacío): {e}")

    print("\n--- 6. RECORRIDO POLIMÓRFICO (Un solo ciclo) ---")
    comunidad = [est1, est2, doc1, doc2, adm1, adm2]
    
    for persona in comunidad:
        # Un solo ciclo invoca ambos métodos
        persona.mostrar_informacion()
        persona.realizar_actividad_principal()
        print("-" * 40)