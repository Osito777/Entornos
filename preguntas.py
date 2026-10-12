"""Banco de preguntas de ENTORNOS DE DESARROLLO (DAW 1.º), basado en ENTORNOS.pptx.

Formato de cada pregunta: q(tema, pregunta, correcta, incorrecta1, incorrecta2, explicacion)
La app mezcla las 3 alternativas cada vez, así que la correcta puede ir en cualquier posición.
"""

T1 = "1. Conceptos básicos"
T2 = "2. Ciclo de vida del software"
T3 = "3. Modelos de desarrollo"
T4 = "4. Lenguajes de programación"
TEMAS = [T1, T2, T3, T4]


def q(tema, pregunta, correcta, mal1, mal2, explicacion=""):
    return {
        "tema": tema,
        "pregunta": pregunta,
        "opciones": [correcta, mal1, mal2],
        "correcta": correcta,
        "explicacion": explicacion,
    }


PREGUNTAS = [
    # ---------------- 1. CONCEPTOS BÁSICOS ----------------
    q(T1, "¿Qué tipo de software es un sistema operativo?", "De sistema", "De aplicación", "De desarrollo", "El sistema operativo y los drivers son software de sistema."),
    q(T1, "Un navegador web es un software...", "De aplicación", "De sistema", "De desarrollo", "Suite ofimática, navegador o edición de imagen son software de aplicación."),
    q(T1, "Los editores, compiladores e intérpretes son software...", "De desarrollo", "De sistema", "De aplicación", "Son las herramientas que se usan para crear otros programas."),
    q(T1, "Los drivers pertenecen al software...", "De sistema", "De aplicación", "De desarrollo", "Los drivers forman parte del software de sistema junto al sistema operativo."),
    q(T1, "El código fuente es...", "Un archivo de texto legible escrito en un lenguaje de programación", "Un archivo binario ejecutable", "Un archivo binario intermedio no ejecutable", "Es el texto que escribe el programador."),
    q(T1, "El código objeto (intermedio) es...", "Un archivo binario no ejecutable", "Un archivo de texto legible por el programador", "Un archivo binario que el sistema ejecuta directamente", "Se obtiene al traducir el código fuente, pero aún no se puede ejecutar."),
    q(T1, "El código ejecutable es...", "Un archivo binario ejecutable", "Un archivo de texto legible", "Un archivo binario no ejecutable", "Es el binario final que el sistema operativo puede ejecutar."),
    q(T1, "¿En qué orden se obtienen los tres tipos de código?", "Fuente, objeto y ejecutable", "Objeto, fuente y ejecutable", "Ejecutable, objeto y fuente", "Se escribe el fuente, se traduce a objeto y se obtiene el ejecutable."),
    q(T1, "¿Qué hace el disco duro respecto a los programas?", "Almacena de forma permanente los archivos ejecutables y de datos", "Almacena de forma temporal el código binario de los ejecutables", "Lee y ejecuta las instrucciones de los programas", "El almacenamiento permanente es función del disco duro."),
    q(T1, "¿Qué función tiene la memoria RAM?", "Almacena temporalmente el código binario de los ejecutables y los datos necesarios", "Almacena de forma permanente los archivos del usuario", "Recoge nuevos datos desde los dispositivos de entrada", "La RAM guarda de forma temporal lo que se está usando."),
    q(T1, "¿Qué hace la CPU?", "Lee y ejecuta las instrucciones almacenadas en la RAM, junto con sus datos", "Almacena de forma permanente los archivos", "Guarda temporalmente los resultados en disco", "La CPU toma las instrucciones de la memoria RAM y las ejecuta."),
    q(T1, "¿Para qué sirven los dispositivos de entrada/salida (E/S)?", "Recogen datos desde la entrada y muestran los resultados", "Ejecutan las instrucciones del programa", "Almacenan permanentemente los programas", "Permiten introducir datos y mostrar resultados, o leer y guardar en disco."),
    q(T1, "¿Dónde se carga el código binario de un programa para que la CPU lo ejecute?", "En la memoria RAM", "En el disco duro", "En los dispositivos de entrada/salida", "El ejecutable se guarda en el disco, pero se ejecuta desde la RAM."),
    q(T1, "¿Cuál es un ejemplo de software de aplicación?", "Una suite ofimática", "Un driver de la tarjeta gráfica", "Un compilador", "La suite ofimática es una aplicación; el driver es de sistema y el compilador de desarrollo."),

    # ---------------- 2. CICLO DE VIDA ----------------
    q(T2, "¿Cuál es el orden correcto de las fases principales del desarrollo de software?", "Análisis, diseño, codificación, pruebas y mantenimiento", "Diseño, análisis, codificación, mantenimiento y pruebas", "Análisis, codificación, diseño, pruebas y mantenimiento", "Es el orden de las fases principales del ciclo de vida."),
    q(T2, "La ingeniería del software es...", "La disciplina que estudia los principios y metodologías para el desarrollo y mantenimiento de sistemas software", "La fase en la que se escribe el código fuente", "El conjunto de pruebas que se hace al programa", "Es una disciplina, no una fase concreta."),
    q(T2, "En la fase de análisis...", "Se definen las necesidades del cliente y se especifican los requisitos", "Se escribe el código fuente", "Se corrigen los defectos detectados", "El análisis determina qué necesita el cliente y qué requisitos debe cumplir el software."),
    q(T2, "¿Qué debe evitar la especificación de requisitos?", "Las ambigüedades y los detalles de diseño o implementación", "Separar requisitos funcionales y no funcionales", "Fijar criterios de validación", "Debe ser clara y no entrar en cómo se diseñará o implementará."),
    q(T2, "La especificación de requisitos debe ser entendible por...", "El cliente", "Solo el programador", "Solo el sistema operativo", "El cliente tiene que poder comprender y validar los requisitos."),
    q(T2, "En la fase de diseño...", "Se descompone el sistema en componentes que pueden desarrollarse por separado", "Se escribe el código de cada componente", "Se prueba el sistema con el usuario", "El diseño organiza el sistema en elementos y define su interrelación."),
    q(T2, "¿Cuál es una actividad habitual de la fase de diseño?", "Diseño de datos", "Pruebas de integración", "Corrección de defectos", "Las actividades son: diseño arquitectónico, detallado, de datos y de interfaz."),
    q(T2, "En la fase de codificación...", "Se escribe el código fuente de cada componente", "Se define lo que necesita el cliente", "Se corrigen defectos tras la entrega", "La codificación convierte el diseño en código."),
    q(T2, "¿Cuál de estos son lenguajes de otro tipo que pueden usarse al codificar (no de programación)?", "HTML, XML y JSON", "C, C++ y Java", "Ensamblador y Prolog", "HTML, XML y JSON no son lenguajes de programación."),
    q(T2, "¿Cuál es el principal objetivo de las pruebas?", "Conseguir que el programa funcione incorrectamente y descubrir defectos", "Demostrar que el programa no tiene ningún error", "Documentar el sistema", "Las pruebas buscan encontrar fallos, no confirmar que todo está bien."),
    q(T2, "Para probar un programa hay que someterlo a...", "El máximo número de situaciones diferentes", "Una única situación típica", "Solo los casos en los que funciona", "Cuantas más situaciones se prueben, más defectos se descubren."),
    q(T2, "El mantenimiento consiste en...", "Realizar cambios ocasionales durante la explotación del sistema", "Escribir el código fuente", "Hacer el análisis inicial de requisitos", "Ocurre cuando el sistema ya está en uso."),
    q(T2, "El mantenimiento correctivo...", "Corrige defectos", "Mejora la funcionalidad", "Adapta el software a nuevos entornos", "Correctivo = se corrigen defectos."),
    q(T2, "El mantenimiento perfectivo...", "Mejora la funcionalidad", "Corrige defectos", "Añade funcionalidades nuevas", "Perfectivo = se mejora la funcionalidad existente."),
    q(T2, "El mantenimiento evolutivo...", "Añade funcionalidades nuevas", "Corrige defectos", "Adapta el software a nuevos entornos", "Evolutivo = se añaden funcionalidades nuevas."),
    q(T2, "El mantenimiento adaptativo...", "Adapta el software a nuevos entornos", "Corrige defectos", "Añade funcionalidades nuevas", "Adaptativo = se adapta a nuevos entornos."),
    q(T2, "¿Qué resultado se obtiene de la ingeniería de sistemas, antes del análisis?", "La especificación del sistema", "El código fuente", "Los informes de errores", "Es el primer resultado de la lista de resultados tras cada fase."),
    q(T2, "¿Qué resultado se obtiene tras la fase de análisis?", "La especificación de requisitos del software", "El código fuente", "El documento de arquitectura del software", "El análisis produce la especificación de requisitos."),
    q(T2, "¿Qué resultado se obtiene del diseño arquitectónico?", "El documento de arquitectura del software", "La especificación de módulos y funciones", "El código fuente", "El diseño arquitectónico genera el documento de arquitectura."),
    q(T2, "¿Qué resultado se obtiene del diseño detallado?", "La especificación de módulos y funciones", "El documento de arquitectura del software", "Un sistema utilizable", "El diseño detallado especifica módulos y funciones."),
    q(T2, "¿Qué resultado se obtiene tras la codificación?", "El código fuente", "Módulos utilizables", "Un sistema aceptado", "Codificar produce código fuente."),
    q(T2, "¿Qué resultado dan las pruebas de unidades?", "Módulos utilizables", "Un sistema utilizable", "Un sistema aceptado", "Probar cada unidad deja módulos utilizables."),
    q(T2, "¿Qué resultado dan las pruebas de integración?", "Un sistema utilizable", "Módulos utilizables", "Un sistema aceptado", "Al integrar los módulos se obtiene un sistema utilizable."),
    q(T2, "¿Qué resultado dan las pruebas del sistema?", "Un sistema aceptado", "Módulos utilizables", "Un sistema utilizable", "Las pruebas del sistema dejan un sistema aceptado."),
    q(T2, "¿Qué resultado se obtiene del mantenimiento?", "Informes de errores y control de cambios", "Documentación técnica y de usuario", "El código fuente", "El mantenimiento genera informes de errores y control de cambios."),
    q(T2, "¿Qué resultado se obtiene de la fase de documentación?", "Documentación técnica y de usuario", "Informes de errores", "Especificación del sistema", "La documentación produce manuales técnicos y de usuario."),
    q(T2, "¿Qué fase se realiza justo después de la codificación?", "Las pruebas", "El diseño", "El análisis", "El orden es análisis, diseño, codificación, pruebas y mantenimiento."),

    # ---------------- 3. MODELOS DE DESARROLLO ----------------
    q(T3, "¿Cuáles son los modelos clásicos (predictivos)?", "Cascada y modelo en V", "Scrum y XP", "Espiral y Kanban", "Los clásicos son el modelo en cascada y el modelo en V."),
    q(T3, "¿Qué modelos se consideran evolutivos o incrementales?", "Espiral y metodologías ágiles", "Cascada y modelo en V", "Solo el modelo en cascada", "Los evolutivos incluyen el modelo en espiral y las metodologías ágiles."),
    q(T3, "¿Cuál es el modelo de mayor antigüedad?", "El modelo en cascada", "El modelo en espiral", "Scrum", "La cascada es el modelo más antiguo."),
    q(T3, "En el modelo en cascada, las fases...", "Se realizan en el orden indicado y el resultado de una es la entrada de la siguiente", "Se realizan en paralelo", "Se realizan en cualquier orden", "Cada fase depende del resultado de la anterior."),
    q(T3, "El modelo en cascada es...", "Rígido y se adapta mal a los cambios continuos de especificaciones", "Muy flexible ante el cambio", "Iterativo, con sprints de 2 a 4 semanas", "Su rigidez es su principal inconveniente."),
    q(T3, "El modelo en V es muy parecido al modelo...", "En cascada", "Scrum", "De prototipos", "Es una variante con visión jerarquizada por niveles."),
    q(T3, "En el modelo en V, los niveles superiores indican...", "Mayor abstracción", "Mayor nivel de detalle", "Menor jerarquía", "Arriba hay más abstracción; abajo, más detalle."),
    q(T3, "Los prototipos se usan porque...", "Los requisitos no están claramente especificados", "Los requisitos son totalmente estables", "No hay cliente", "El prototipo ayuda a refinar los requisitos."),
    q(T3, "En el modelo de prototipos...", "Se crea un prototipo en el análisis, el cliente lo prueba y se refinan los requisitos, repitiéndolo si hace falta", "Se programa el sistema completo y se prueba al final", "Se elimina la participación del cliente", "El proceso se repite las veces necesarias."),
    q(T3, "Los prototipos rápidos...", "Pueden usar otro lenguaje o herramientas y finalmente se desechan", "Se usan como base para desarrollar el proyecto", "Se diseñan siempre con el mismo lenguaje del proyecto", "Son prototipos desechables."),
    q(T3, "Los prototipos evolutivos...", "Se diseñan con el mismo lenguaje y herramientas del proyecto y sirven de base", "Se desechan al terminar", "Usan siempre otro lenguaje", "Se convierten en la base del proyecto."),
    q(T3, "¿Quién desarrolló el modelo en espiral y en qué año?", "Boehm, en 1988", "Toyota, en 1988", "El Manifiesto Ágil, en 1988", "El modelo en espiral fue desarrollado por Boehm en 1988."),
    q(T3, "El modelo en espiral aplicado a la programación orientada a objetos destaca...", "La reutilización de código", "La eliminación de las pruebas", "La documentación extensiva", "En la actividad de ingeniería se da gran importancia a reutilizar código."),
    q(T3, "Las metodologías ágiles se basan en...", "El desarrollo iterativo e incremental", "Una planificación rígida con fases fijas", "Un único ciclo sin cambios", "Los requisitos y soluciones evolucionan con el tiempo."),
    q(T3, "En los métodos ágiles, los requisitos y soluciones...", "Evolucionan con el tiempo según la necesidad del proyecto", "Se fijan al inicio y no cambian", "Los decide solo el Scrum Master", "Los equipos son auto-organizados y trabajan con decisiones a corto plazo."),
    q(T3, "Las metodologías ágiles más conocidas son...", "Kanban, Scrum y XP", "Cascada, V y espiral", "Prolog, Lisp y SQL", "Kanban, Scrum y XP (eXtreme Programming)."),
    q(T3, "El Manifiesto Ágil valora más...", "Individuos e interacciones sobre procesos y herramientas", "Procesos y herramientas sobre individuos", "Documentación extensiva sobre software funcionando", "Prioriza las personas sobre los procesos."),
    q(T3, "Kanban también se denomina...", "Sistema de tarjetas", "Programación extrema", "Modelo en espiral", "Kanban es el sistema de tarjetas."),
    q(T3, "¿Quién desarrolló Kanban inicialmente?", "Toyota, para la industria de fabricación", "Boehm", "Microsoft", "Nació en Toyota (lean manufacturing)."),
    q(T3, "¿Cuáles son las columnas típicas de una pizarra Kanban?", "To do, Doing y Done", "Análisis, Diseño y Codificación", "Product Owner, Scrum Master y Team", "Por hacer, en proceso y hecho."),
    q(T3, "Scrum es un modelo de desarrollo...", "Incremental", "Predictivo y secuencial", "Basado en un único prototipo", "Trabaja por iteraciones (sprints)."),
    q(T3, "¿Cuánto suelen durar las iteraciones (sprints) de Scrum?", "2, 3 o 4 semanas", "1 día", "6 meses", "Los sprints son regulares, de 2 a 4 semanas."),
    q(T3, "El Sprint Backlog es...", "La lista de requisitos sacados del backlog para desarrollarlos durante el sprint", "La lista global de requisitos del producto", "El estado del producto tras cada sprint", "Es un subconjunto del Product Backlog."),
    q(T3, "Al finalizar cada iteración de Scrum se obtiene...", "Una entrega parcial utilizable por el cliente", "Solo documentación", "El producto terminado siempre", "Cada sprint deja un incremento utilizable."),
    q(T3, "El Product Owner es...", "La voz del cliente: define los criterios de aceptación", "Quien asegura que se sigue Scrum", "El equipo de desarrollo", "Define y asegura el cumplimiento de los criterios de aceptación."),
    q(T3, "El Scrum Master...", "Asegura que se sigue la metodología y facilita el trabajo del equipo", "Es la voz del cliente", "Programa todo el código", "Motiva y facilita el trabajo del equipo."),
    q(T3, "El Team de Scrum es...", "Un equipo auto-organizado y multifuncional de entre 6 y 10 miembros", "Una sola persona", "El cliente", "Es el equipo de desarrollo."),
    q(T3, "El Product Backlog es...", "La lista ordenada con los requisitos del producto", "La lista de requisitos de un único sprint", "El estado del producto tras cada sprint", "Contiene todos los requisitos del producto."),
    q(T3, "El Incremento es...", "El estado del producto después de cada sprint", "La lista ordenada de requisitos", "La reunión diaria", "Es el artefacto que muestra el avance tras cada sprint."),
    q(T3, "¿Cuál es la duración máxima del Daily Scrum?", "15 minutos", "8 horas", "1 mes", "Es una reunión diaria muy breve."),
    q(T3, "¿Cuál es la duración máxima del Sprint Planning?", "8 horas", "15 minutos", "3 horas", "Es la reunión inicial donde se planifica el trabajo del sprint."),
    q(T3, "¿Cuál es la duración máxima de la Scrum Review?", "4 horas", "15 minutos", "1 mes", "Sirve para evaluar el incremento obtenido."),
    q(T3, "¿Para qué sirve la Scrum Retrospective?", "Para evaluar la correcta aplicación de la metodología Scrum", "Para planificar el trabajo del sprint", "Para evaluar el incremento con el cliente", "Su duración máxima es de 3 horas."),
    q(T3, "XP significa...", "Programación extrema (eXtreme Programming)", "Extended Production", "Experimental Process", "XP es la programación extrema."),
    q(T3, "¿Cuáles son los valores de XP?", "Simplicidad, comunicación, retroalimentación, valentía y respeto", "Rigidez, aislamiento y documentación", "Velocidad, secreto y jerarquía", "Son los cinco valores de la programación extrema."),
    q(T3, "¿Cuál es una característica de XP?", "La programación por parejas", "Las fases rígidas", "La documentación extensiva antes de codificar", "También: diseño sencillo, integración continua y estándares de codificación."),
    q(T3, "En XP, la semana de trabajo es de...", "40 horas semanales", "60 horas semanales", "20 horas semanales", "XP propone 40 horas semanales."),
    q(T3, "En XP, la propiedad del código es...", "Compartida", "Exclusiva de cada programador", "Del cliente", "Cualquier miembro del equipo puede modificar el código."),

    # ---------------- 4. LENGUAJES DE PROGRAMACIÓN ----------------
    q(T4, "Para obtener código binario ejecutable hay dos opciones:", "Compilar o interpretar", "Documentar o probar", "Diseñar o codificar", "Un programa se compila o se interpreta."),
    q(T4, "La compilación/interpretación del código fuente se lleva a cabo en dos fases:", "Análisis léxico y análisis sintáctico", "Análisis semántico y análisis lógico", "Diseño y pruebas", "Si no hay errores, se genera el código objeto."),
    q(T4, "Según el curso, en el proceso de compilación/interpretación...", "No se realiza un análisis semántico", "Se realiza un análisis semántico completo", "Solo se hace el análisis léxico", "Un código bien escrito puede no funcionar como se desea."),
    q(T4, "¿Cuáles son ejemplos de lenguajes compilados?", "C y C++", "PHP y JavaScript", "Prolog y SQL", "C y C++ son lenguajes compilados."),
    q(T4, "¿Cuál es la principal ventaja de los lenguajes compilados?", "Su ejecución es muy eficiente", "El código fuente se interpreta directamente", "No hace falta compilar al modificar el código", "Su eficiencia es su ventaja principal."),
    q(T4, "¿Cuál es la principal desventaja de los lenguajes compilados?", "Hay que compilar cada vez que se modifica el código fuente", "Su ejecución es menos eficiente", "No existen para el lenguaje C", "Cada cambio exige volver a compilar."),
    q(T4, "¿Cuáles son ejemplos de lenguajes interpretados?", "PHP y JavaScript", "C y C++", "Ensamblador y C", "PHP y JavaScript son interpretados."),
    q(T4, "¿Cuál es la principal ventaja de los lenguajes interpretados?", "El código fuente se interpreta directamente", "Su ejecución es muy eficiente", "Generan siempre bytecode", "No necesitan compilarse antes."),
    q(T4, "¿Cuál es la principal desventaja de los lenguajes interpretados?", "Su ejecución es menos eficiente", "Hay que compilar cada vez que se modifica el código", "Solo funcionan en un sistema operativo", "Interpretar es menos eficiente que ejecutar código compilado."),
    q(T4, "Java es un lenguaje...", "Compilado e interpretado", "Solo compilado", "Solo interpretado", "Se compila a bytecode y luego se interpreta."),
    q(T4, "El bytecode de Java es...", "Código binario intermedio destinado a la máquina virtual de Java", "El código fuente en texto", "Código nativo del procesador", "Puede considerarse código objeto, pero para la máquina virtual."),
    q(T4, "¿Cuáles son ventajas de Java?", "Es estructurado, orientado a objetos y relativamente fácil de aprender", "Es el lenguaje más eficiente que existe", "No necesita documentación", "También tiene buena documentación y base de usuarios."),
    q(T4, "¿Cuál es una desventaja de Java?", "Es menos eficiente que los lenguajes compilados", "Es muy difícil de aprender", "No tiene comunidad de usuarios", "Su ejecución es menos eficiente que la de los compilados."),
    q(T4, "Según la forma en la que operan, los lenguajes se dividen en...", "Declarativos e imperativos", "Compilados e interpretados", "Fuente y objeto", "Declarativos: el resultado; imperativos: los pasos."),
    q(T4, "En un lenguaje declarativo...", "Indicamos el resultado a obtener sin especificar los pasos", "Indicamos los pasos a seguir", "Escribimos directamente código binario", "Los imperativos son los que indican los pasos."),
    q(T4, "Los lenguajes declarativos lógicos...", "Utilizan reglas, como Prolog", "Utilizan funciones, como Lisp", "Utilizan sentencias, como SQL", "Lógicos = reglas (Prolog)."),
    q(T4, "SQL es un lenguaje...", "Declarativo de tipo algebraico", "Imperativo estructurado", "De bajo nivel", "Los algebraicos utilizan sentencias, como SQL."),
    q(T4, "¿Qué lenguajes son multiparadigma?", "C++ y JavaScript", "C y Java", "Prolog y SQL", "C++ y JavaScript son lenguajes imperativos multiparadigma."),
    q(T4, "Según su nivel de abstracción, el ensamblador es un lenguaje de...", "Bajo nivel", "Medio nivel", "Alto nivel", "Ensamblador = bajo nivel; C = medio; C++ y Java = alto nivel."),
    q(T4, "¿Qué lenguajes son de alto nivel?", "C++ y Java", "Ensamblador", "Código binario", "C++ y Java son de alto nivel."),
    q(T4, "¿Cuál es el orden de evolución de los lenguajes?", "Código binario, ensamblador, estructurados y orientados a objetos", "Orientados a objetos, estructurados, ensamblador y código binario", "Ensamblador, código binario, orientados a objetos y estructurados", "Los lenguajes han ido evolucionando hacia niveles de abstracción mayores."),
]

if __name__ == "__main__":
    print(len(PREGUNTAS), "preguntas")
    for t in TEMAS:
        print(t, sum(1 for p in PREGUNTAS if p["tema"] == t))
