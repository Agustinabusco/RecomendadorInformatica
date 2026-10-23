# Define una función que muestra la presentación del programa.
def mostrar_presentacion():
    # Muestra el nombre del sistema.
    print("RECOMENDADOR DE ACTIVIDADES DE INFORMÁTICA")

    # Explica para qué sirve.
    print("Te ayudamos a elegir una actividad para practicar Python.")

# Llama a la función para mostrar la presentación.
mostrar_presentacion()

print()

# Muestra los temas disponibles.
print("¿Qué tema querés practicar?")
print("1. Mostrar mensajes y operaciones con print()")
print("2. Variables")
print("3. Condicionales: if y else")

# Pide una opción y guarda lo escrito en la variable tema.
tema = input("Escribí el número de tu opción: ")

# Muestra la opción ingresada para comprobar que se guardó.
print("Elegiste la opción:", tema)

print()

# Muestra los tipos de ayuda disponibles.
print("¿Qué necesitás trabajar?")
print("1. Comprender cómo funciona el tema")
print("2. Practicar cómo escribir el código")

# Guarda la respuesta del estudiante en la variable dificultad.
dificultad = input("Escribí el número de tu opción: ")

# Muestra la respuesta para comprobar que se guardó.
print("Elegiste la dificultad:", dificultad)

# Comprueba si el estudiante eligió print() y comprender el tema.
# Las dos condiciones deben cumplirse para mostrar esta recomendación.
if tema == "1" and dificultad == "1":
    print()
    print("ACTIVIDAD RECOMENDADA")
    print("Observá estas instrucciones y anticipá qué mostrará cada una:")

    # Muestra ejemplos como texto, sin ejecutarlos.
    print('print("Hola")')
    print('print(3 + 2)')
    print('print("3 + 2")')

    print("Después, ejecutalas en otro archivo y compará los resultados.")

    # Explica por qué el sistema seleccionó esta actividad.
    print("Motivo: elegiste print() y necesitás comprender cómo funciona.")
    
    # Si eligió print() y practicar cómo escribir código.
elif tema == "1" and dificultad == "2":
    print()
    print("ACTIVIDAD RECOMENDADA")
    print("Escribí un programa de dos líneas:")
    print("1. Mostrá un mensaje breve elegido por vos.")
    print("2. Mostrá el resultado de sumar dos números.")
    print("Antes de ejecutarlo, anticipá qué aparecerá en pantalla.")
    print("Motivo: elegiste print() y necesitás practicar cómo escribir código.")

# Si eligió variables y comprender cómo funcionan.
elif tema == "2" and dificultad == "1":
    print()
    print("ACTIVIDAD RECOMENDADA")
    print("Leé este código y anticipá qué valor se mostrará:")
    print("puntos = 2")
    print("puntos = puntos + 3")
    print("print(puntos)")
    print("Explicá qué valor tiene puntos antes y después de la suma.")
    print("Después, ejecutá el código en otro archivo para comprobarlo.")
    print("Motivo: elegiste variables y necesitás comprender cómo funcionan.")

# Si eligió variables y practicar cómo escribir código.
elif tema == "2" and dificultad == "2":
    print()
    print("ACTIVIDAD RECOMENDADA")
    print("Creá una variable llamada nombre y otra llamada edad.")
    print("Guardá tu nombre y tu edad en ellas.")
    print("Después, mostrá sus valores usando print().")
    print("Recordá escribir tu nombre entre comillas.")
    print("Motivo: elegiste variables y necesitás practicar cómo escribir código.")

# Si eligió condicionales y comprender cómo funcionan.
elif tema == "3" and dificultad == "1":
    print()
    print("ACTIVIDAD RECOMENDADA")
    print("Leé este código:")
    print("puntos = 3")
    print("if puntos >= 5:")
    print('    print("¡Ganaste!")')
    print("else:")
    print('    print("Te faltan puntos")')
    print("¿Qué mensaje aparecerá? ¿Y si puntos vale 5?")
    print("Después, probá ambos valores en otro archivo.")
    print("Motivo: elegiste condicionales y necesitás comprender cómo funcionan.")

# Si eligió condicionales y practicar cómo escribir código.
elif tema == "3" and dificultad == "2":
    print()
    print("ACTIVIDAD RECOMENDADA")
    print("Creá una variable llamada puntos y asignale un número.")
    print("Usá if y else para mostrar:")
    print("- ¡Ganaste!, si puntos es igual o mayor que 5.")
    print("- Te faltan puntos, en caso contrario.")
    print("Probá el programa con los valores 3, 5 y 8.")
    print("Motivo: elegiste condicionales y necesitás practicar cómo escribir código.")

# Si ninguna regla coincide, informa que alguna opción no es válida.
else:
    print()
    print("Alguna opción no es válida.")
    print("Elegí un tema del 1 al 3 y una dificultad del 1 al 2.")