# Presenta el programa al comenzar.
def mostrar_presentacion():
    print("RECOMENDADOR DE ACTIVIDADES DE INFORMÁTICA")
    print("Te ayudamos a elegir una actividad para practicar Python.")


# Recibe una pregunta y las opciones permitidas.
# Repite la pregunta hasta obtener una respuesta válida.
def pedir_opcion(mensaje, opciones_validas):
    # input devuelve texto; strip elimina espacios de los extremos.
    opcion = input(mensaje).strip()

    # Si la opción no está entre las permitidas, vuelve a preguntar.
    while opcion not in opciones_validas:
        print("Opción no válida. Intentá nuevamente.")
        opcion = input(mensaje).strip()

    # Entrega la respuesta válida al lugar donde se llamó a la función.
    return opcion


# Aplica las seis reglas usando el tema y la dificultad recibidos.
# Estas reglas representan el conocimiento del sistema para recomendar.
def recomendar_actividad(tema, dificultad):
    print()
    print("ACTIVIDAD RECOMENDADA")

    # Regla 1: print() y comprensión.
    # and exige que las dos condiciones se cumplan.
    if tema == "1" and dificultad == "1":
        print("Observá estas instrucciones y anticipá qué mostrará cada una:")

        # Los ejemplos se muestran como texto; aquí no se ejecutan.
        print('print("Hola")')
        print('print(3 + 2)')
        print('print("3 + 2")')

        print("Después, ejecutalas en otro archivo y compará los resultados.")
        print("Motivo: elegiste print() y necesitás comprender cómo funciona.")

    # Regla 2: print() y escritura de código.
    elif tema == "1" and dificultad == "2":
        print("Escribí un programa de dos líneas:")
        print("1. Mostrá un mensaje breve elegido por vos.")
        print("2. Mostrá el resultado de sumar dos números.")
        print("Antes de ejecutarlo, anticipá qué aparecerá en pantalla.")
        print("Motivo: elegiste print() y necesitás practicar cómo escribir código.")

    # Regla 3: variables y comprensión.
    elif tema == "2" and dificultad == "1":
        print("Leé este código y anticipá qué valor se mostrará:")
        print("puntos = 2")
        print("puntos = puntos + 3")
        print("print(puntos)")
        print("Explicá qué valor tiene puntos antes y después de la suma.")
        print("Después, ejecutá el código en otro archivo para comprobarlo.")
        print("Motivo: elegiste variables y necesitás comprender cómo funcionan.")

    # Regla 4: variables y escritura de código.
    elif tema == "2" and dificultad == "2":
        print("Creá una variable llamada nombre y otra llamada edad.")
        print("Guardá tu nombre y tu edad en ellas.")
        print("Después, mostrá sus valores usando print().")
        print("Recordá escribir tu nombre entre comillas.")
        print("Motivo: elegiste variables y necesitás practicar cómo escribir código.")

    # Regla 5: condicionales y comprensión.
    elif tema == "3" and dificultad == "1":
        print("Leé este código:")
        print("puntos = 3")
        print("if puntos >= 5:")
        print('    print("¡Ganaste!")')
        print("else:")
        print('    print("Te faltan puntos")')
        print("¿Qué mensaje aparecerá? ¿Y si puntos vale 5?")
        print("Después, probá ambos valores en otro archivo.")
        print("Motivo: elegiste condicionales y necesitás comprender cómo funcionan.")

    # Regla 6: condicionales y escritura de código.
    elif tema == "3" and dificultad == "2":
        print("Creá una variable llamada puntos y asignale un número.")
        print("Usá if y else para mostrar:")
        print("- ¡Ganaste!, si puntos es igual o mayor que 5.")
        print("- Te faltan puntos, en caso contrario.")
        print("Probá el programa con los valores 3, 5 y 8.")
        print("Motivo: elegiste condicionales y necesitás practicar cómo escribir código.")

    # Respaldo si se llama a esta función con una combinación no prevista.
    # En el uso normal, pedir_opcion ya impide esas entradas.
    else:
        print("No hay una recomendación para esa combinación.")


# Diccionario: cada clave es una opción y cada valor es el nombre del tema.
temas = {
    "1": "Mostrar mensajes y operaciones con print()",
    "2": "Variables",
    "3": "Condicionales: if y else"
}

# Comienza la ejecución del programa.
mostrar_presentacion()

# La opción 1 permite comenzar y realizar nuevas consultas.
continuar = "1"

# Repite la consulta mientras el estudiante elija continuar.
while continuar == "1":
    print()
    print("¿Qué tema querés practicar?")

    # items permite recorrer las claves y los valores del diccionario.
    for numero, nombre in temas.items():
        print(numero + ". " + nombre)

    # En un diccionario, la validación comprueba sus claves: 1, 2 y 3.
    tema = pedir_opcion("Escribí el número de tu opción: ", temas)

    print()
    print("¿Qué necesitás trabajar?")
    print("1. Comprender cómo funciona el tema")
    print("2. Practicar cómo escribir el código")

    # La lista contiene las únicas respuestas permitidas para esta pregunta.
    dificultad = pedir_opcion("Escribí el número de tu opción: ", ["1", "2"])

    # Envía ambas respuestas a la función que aplica las reglas.
    recomendar_actividad(tema, dificultad)

    print()
    print("¿Querés realizar otra consulta?")
    print("1. Sí")
    print("2. No, salir")

    # Si devuelve 2, la condición del while deja de cumplirse.
    continuar = pedir_opcion("Escribí el número de tu opción: ", ["1", "2"])

# Se muestra cuando termina el ciclo de consultas.
print("Gracias por usar el recomendador. ¡Hasta la próxima!")