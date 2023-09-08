# Trabajo Práctico I - Programación II
import bibloteca
import os


print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Préstamo")
    print("2 - Gestionar Devolución")
    print("3 - Registrar nuevo libro")
    print("4 - Eliminar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls")                                       #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            # Préstamo de un libro. Se ingresa el código del libro/Busca/Muestra/Valida/Actualiza el stock de prestados/Visualiza
            bibloteca.prestar_ejemplar_libro()
            print()
        elif int(opt) == 2:
            # Devolución del libro. Se ingresa el código del libro/Busca/Valida/Actualiza el stock de prestados/Visualiza
            bibloteca.devolver_ejemplar_libro()
            print()
        elif int(opt) == 3:
            # Alta libro. Se ingresan los datos del nuevo libro/Genera código/Agrega libro
            bibloteca.registrar_nuevo_libro()
            print()
        elif int(opt) == 4:
            # Baja libro. Se ingresa el código del libro a eliminar/Baja un ejemplar del stock
            bibloteca.eliminar_ejemplar_libro()
            print()
        elif int(opt) == 5:
            # Visualiza libros
            bibloteca.ejemplares_prestados()
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....")    # Pausa

print("Hasta luego!.")