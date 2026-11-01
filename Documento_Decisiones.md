# Documento de Decisiones de Diseño - Actividad Colaborativa N°2

**Universidad de Manizales**  
**Facultad de Ciencias e Ingenierías**  
**Programa:** Ingeniería en Analítica de Datos  
**Asignatura:** Programación I  
**Integrante:** Johan Sebastian Ardila Rueda (sebasruar)  
**Fecha:** Noviembre de 2026

## Introducción
Con este documento quiero explicar el por qué tomé ciertas decisiones en la Actividad 2. La idea es mostrar cómo evolucionó el sistema de la Actividad 1, agregando clases abstractas, composición y excepciones personalizadas para que el sistema de matrícula funcione bien.

## Descripción general de la solución implementada
El sistema permite registrar personas (estudiantes, docentes y administrativos), programas, asignaturas y ahora también grupos académicos. Para esta segunda versión, creé las clases `Horario`, `GrupoAcademico` y `SistemaAcademico`, que se encargan de organizar la oferta académica y manejar la matrícula. También agregué excepciones personalizadas para que el programa no se caiga cuando alguien comete un error (como matricular dos veces al mismo estudiante).

## Desarrollo

### 1. ¿Por qué la clase Persona es abstracta?
La hice abstracta porque en la universidad no tiene sentido registrar a alguien solo como "Persona". Siempre tiene que ser estudiante, docente o administrativo. Entonces, al heredar de `ABC` y poner el método `realizar_actividad_principal()` como `@abstractmethod`, obligo a que las clases hijas implementen ese método. Así me aseguro de que cada tipo de persona tenga su propio comportamiento y no se puedan crear "personas genéricas".

### 2. ¿Qué hace cada clase derivada?
`Estudiante`, `Docente` y `Administrativo` heredan de `Persona` e implementan `realizar_actividad_principal()` a su manera:
- El **Estudiante** dice qué programa cursa y en qué semestre va.
- El **Docente** dice en qué facultad orienta clases.
- El **Administrativo** dice qué cargo tiene y en qué dependencia trabaja.

Así, aunque el método se llame igual, cada uno responde distinto según su rol.

### 3. ¿Cómo se relacionan las clases del sistema?
La clase `GrupoAcademico` es el centro de todo. Recibe un objeto `Asignatura` y un objeto `Docente` ya creados (no textos sueltos), y los valida con `isinstance` para que no le pasen cualquier cosa. También tiene una lista privada de estudiantes matriculados (`__estudiantes_matriculados`) y crea su propio `Horario` por dentro.

### 4. ¿Por qué el horario es composición y no herencia?
Porque el horario se crea **dentro** del grupo académico, en su constructor. No es que el grupo "herede" de horario; es que el grupo **tiene un** horario. Si el grupo desaparece, el horario también. Esa es la diferencia clave: la composición es cuando una clase contiene a otra y depende de ella para existir.

### 5. ¿Qué controla cada excepción?
- `EstudianteDuplicadoError`: se lanza en `matricular_estudiante()` si el estudiante ya está en el grupo. Se compara por `codigo_estudiantil` para que no importe si es el mismo objeto o no.
- `CapacidadMaximaError`: se lanza en `matricular_estudiante()` si el grupo ya está lleno.
- `EstudianteNoMatriculadoError`: se lanza en `retirar_estudiante()` si el estudiante no está en la lista.
- `AsignaturaNoEncontradaError` y `ProgramaNoEncontradoError`: se lanzan en `SistemaAcademico.buscar_asignatura()` y `buscar_programa()` si el código no existe.

Todas se capturan en el `main.py` con `try/except`, para que el programa siga funcionando aunque ocurra un error.

### 6. ¿Cómo se mantiene el polimorfismo de la Actividad 1?
Se mantiene con la lista `comunidad` en el `main.py`. Ahí guardo 6 objetos (2 estudiantes, 2 docentes y 2 administrativos) y los recorro con un solo ciclo `for`. En lugar de usar `if` para preguntar de qué tipo es cada uno, simplemente le digo a cada `persona` que ejecute `mostrar_informacion()` y `realizar_actividad_principal()`. Python se encarga de ejecutar el método correcto según el tipo real del objeto.

## Conclusiones
Al terminar esta actividad, siento que entendí mucho mejor cómo funciona la Programación Orientada a Objetos en un caso real. En la Actividad 1 ya había hecho las clases base, pero en esta segunda parte me tocó enfrentarme a cosas nuevas como las clases abstractas, la composición y las excepciones personalizadas.

Con lo de la clase abstracta, al principio me enredé un poco porque no entendía por qué no podía crear una `Persona` directamente. Pero después de leer y practicar, entendí que tiene todo el sentido: en la universidad no existe una persona "genérica", siempre es estudiante, docente o administrativo. Entonces, al obligar a las clases hijas a implementar `realizar_actividad_principal()`, me aseguro de que cada una tenga su propio comportamiento y no se pueda crear un objeto sin identidad clara.

La composición también fue un concepto interesante. Antes pensaba que todo se resolvía con herencia, pero aquí me di cuenta de que un grupo académico no es un horario, sino que lo contiene. Es como si el grupo tuviera un horario adentro. Eso me ayudó a entender que la composición es cuando una clase depende de otra para existir, y que es diferente a la herencia.

Las excepciones personalizadas fueron quizás lo que más me costó, pero también lo que más me sirvió. Antes solo usaba `if` para validar, pero ahora aprendí a lanzar errores propios como `EstudianteDuplicadoError` o `CapacidadMaximaError`, y a capturarlos con `try/except` para que el programa no se caiga. Eso hace que el sistema sea mucho más robusto y que el usuario reciba mensajes claros cuando algo sale mal.

Finalmente, el polimorfismo de la Actividad 1 sigue intacto. La lista `comunidad` con 6 personas y un solo ciclo `for` demuestra que puedo recorrer objetos de diferentes tipos sin usar `if` ni preguntar de qué clase son. Python solito sabe qué método ejecutar. Eso me parece muy elegante y me da confianza para seguir programando.

En resumen, esta actividad me ayudó a entender que la POO no es solo escribir clases, sino pensar en cómo se relacionan, cómo se protegen los datos y cómo se manejan los errores. Me llevo varios aprendizajes que seguro me van a servir en futuras actividades.