print("¡Bienvenidos a la calculadora!c")
print("Las operaciones disponibles son: suma, multi, div y resta")
print('Si deseas salir, escribe "salir" ahora.')

respuesta = input("¿Deseas continuar? (presiona Enter para seguir o escribe 'salir'): ").lower()

if respuesta == "salir":
    print("¡Hasta luego!")
else:
    num1 = float(input("Ingresa un número: "))
    num2 = float(input("Ingresa el otro número: "))
    operacion = input("Ingresa la operación: ").lower()

    if operacion == "suma":
        print("El resultado es:", num1 + num2)
    elif operacion == "resta":
        print("El resultado es:", num1 - num2)
    elif operacion == "multi":
        print("El resultado es:", num1 * num2)
    elif operacion == "div":
        if num2 != 0:
            print("El resultado es:", num1 / num2)
        else:
            print("Error: no se puede dividir entre cero.")
    else:
        print("Operación no válida.")