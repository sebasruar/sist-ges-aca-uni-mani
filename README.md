# Sistema de Gestión Académica - Actividad Colaborativa #1

**Universidad de Manizales**  
**Facultad de Ciencias e Ingenierías**  
**Programa:** Ingeniería en Analítica de Datos  
**Asignatura:** Programación I  

**Integrante:** Johan Sebastian Ardila Rueda (sebasruar)  

## Descripción general
Se realiza este proyecto, el cual es la primera versión de un sistema de gestión académica que se desarrolla en Python. Este nos permite realizar registros y consultas de información de la comunidad académica (estudiantes, docentes y personal administrativo), de los programas académicos y de las asignaturas, que pertenecen a un programa.

Todas las personas comparten datos generales, los cuales son identificación, nombre y correo. Cada tipo agrega los suyos: el estudiante su código estudiantil, programa, semestre y promedio; el docente su número de empleado, facultad, tipo de contratación y horas semanales; y el administrativo su número de empleado, dependencia, cargo y jornada.

Los atributos se protegen con validaciones, y el archivo `main.py` demuestra cómo funciona el sistema: creación de objetos, modificaciones válidas, intentos de valores inválidos y un recorrido de todas las personas con un único ciclo.

## Estructura de los archivos
```text
sist-ges-aca-uni-mani/
│
├── modelos/
│   ├── __init__.py
│   ├── persona.py
│   ├── programa_academico.py
│   ├── asignatura.py
│   ├── estudiante.py
│   ├── docente.py
│   └── administrativo.py
│
├── main.py
├── .gitignore
└── README.md
```

## Instrucciones para ejecutar
1. Asegúrate de tener Python instalado (versión 3.10 o superior).
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal con el comando:
   `python main.py`

## Explicación de los conceptos POO aplicados

**Encapsulamiento:**
El encapsulamiento sirve para proteger los atributos de las clases u objetos. Cuando usamos `__` (doble guion bajo) en Python, indicamos que son privados y no se pueden cambiar o modificar directamente desde afuera. Para modificarlos de manera segura usamos los `@setter`, que actúan como un filtro y solo permiten realizar cambios válidos. Las validaciones que aplicamos son: correo no vacío, semestres y créditos mayores a cero, promedio entre 0.0 y 5.0. Si el valor no cumple, se lanza un `ValueError`.

**Herencia:**
Al momento de crear personas, la cual es la base general, se le asignaron datos comunes como (ID, nombre, correo). Ahora, cuando se crea un estudiante con `class Estudiante(Persona):`, el estudiante va a heredar esos datos. Al usar `super().__init__(...)` llamamos al constructor de `Persona` para que guarde los datos comunes. Así el estudiante solo se va a encargar de guardar lo suyo, lo cual sería (código estudiantil, programa, semestre y promedio).

**Sobrescritura:**
Usamos `super().mostrar_informacion()` para traer la información ya establecida en la clase `Persona` (ID, nombre y correo) y evitar repetir código. Si usáramos el `print` en cada clase, se repetiría muchas veces. Al usar `super()`, si algún día cambiamos algo en los datos generales de `Persona`, automáticamente donde usamos `super()` se actualizará. Por otro lado, aunque `realizar_actividad_principal()` se llama igual en todas las clases, cada una lo sobrescribe con su propio mensaje. En el Estudiante, imprime que cursa un programa y está en un semestre. En el Docente, imprime que orienta clases en una facultad. En el Administrativo, imprime el cargo que desempeña y la dependencia en la que trabaja.

**Polimorfismo:**
En el `main.py` creo una lista llamada `comunidad` donde guardo 6 objetos (2 estudiantes, 2 docentes y 2 administrativos). Luego uso un solo ciclo `for` para recorrer esa lista. En lugar de usar `if` para preguntar si es estudiante o docente, simplemente le pido a cada `persona` que ejecute `mostrar_informacion()` y `realizar_actividad_principal()`. Python automáticamente reconoce el tipo de objeto y ejecuta el método que le corresponde, sin necesidad de condicionales.

## Uso de herramientas de Inteligencia Artificial
Se utilizaron herramientas de IA como apoyo durante el desarrollo:

- **DeepSeek:** planeación por fases y generación del código base de las clases, que fui validando paso a paso.
- **Claude:** revisión del código frente a los requerimientos del documento, aclaración de conceptos, esqueletos y pistas, y sugerencias de redacción para el README.

Probé, corregí y ejecuté el código en VS Code, y repasé los conceptos (herencia, `super()`, encapsulamiento y polimorfismo) para poder explicarlos con mis propias palabras.

Además, vi videos cortos en TikTok que me ayudaron a entender de forma práctica los conceptos de POO.