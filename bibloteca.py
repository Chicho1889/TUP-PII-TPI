import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # Opción 5 del menú ppal - Visualiza la cantidad de libros prestados de cada uno
    print("*****************************************************************************************************************************")
    print("Código  Título/Nombre                                        Autor                Nº libros prestados      Nº total de libros")
    print("*****************************************************************************************************************************")
    for libro in libros:
        codigo=libro["cod"]
        cantidad=libro["cant_ej_ad"]
        cant_prestados=libro["cant_ej_pr"]
        nombre=libro["titulo"]
        autor=libro["autor"]

        if cant_prestados==0:
            print("-----------------------------------------------------------------------------------------------------------------------------")
            print(f"El libro {nombre}, cuyo código es {codigo}, no tiene préstamos registrados.")
            print("-----------------------------------------------------------------------------------------------------------------------------")
        else:
            print(f"{codigo}   {nombre}                             {autor}               {cant_prestados}                   {cantidad}")
    return None

def registrar_nuevo_libro():
    # Opción 3 del menú principal - "Registrar nuevo libro"
    alta_nuevo_libro=l.nuevo_libro()    # Carga de datos realizada en la función nuevo_libro() ubicada en libro.py
    if alta_nuevo_libro:                # si no viene vacío
        libros.append(alta_nuevo_libro)
        print("")
        print("Los nuevos libros han sido agregados al registro de la biblioteca")
    else:
        print("No se realizó ningún alta por elección del usuario")
    return None

def eliminar_ejemplar_libro():
    # Opción 4 del menú principal - "Eliminar ejemplar"
    codigo_a_borrar=input("Por favor ingrese el código a eliminar: ")
    for libro in libros:
        if codigo_a_borrar==libro["cod"]:
            if libro["cant_ej_ad"]==0:
                print("No hay ejemplares para dar de baja. Se han prestado todos los ejemplares de este libro o se dieron de baja todos los libros, por favor verifique.")
            else:
                stock=libro["cant_ej_ad"]
                print(f"Se ha quitado una unidad del stock total de ese libro que era de {stock} unidades. *Código del libro: {codigo_a_borrar}")
                libro["cant_ej_ad"]-=1
                print("Total actualizado de unidades en stock de ese libro es: ")
                print(libro["cant_ej_ad"])
            return
    print(f"El código ingresado: {codigo_a_borrar} no se encuentra asignado a ningún libro existente, verifique.\n")
    return None

def prestar_ejemplar_libro():
    # Opción 1 del menú - Presta un libro - Resta uno al stock de libros prestados
    codigo_a_buscar=input("Por favor ingrese el código del libro que a prestar: ")
    for libro in libros:
        if codigo_a_buscar==libro["cod"]:
            if libro["cant_ej_ad"]==0:
                print("Lamentablemente no hay stock de ese libro, se han prestado todos los ejemplares disponibles")
            else:
                libro["cant_ej_ad"]-=1
                print(f"El stock de libros del código: {codigo_a_buscar} fue actualizado, ahora hay disponibles para prestar un total de: ")
                print(libro["cant_ej_ad"])
                libro["cant_ej_pr"]+=1
                print(f"Los prestamos totales efectuados del código: {codigo_a_buscar} es de: ")
                print(libro["cant_ej_pr"])
            return
    print(f"El código ingresado: {codigo_a_buscar} no se encuentra asignado a ningún libro existente, verifique.\n")
    
    return None

def devolver_ejemplar_libro():
    # Opción 2 del menú - Devuelve un libro - Agregar uno al stock de libros prestados
    codigo_a_buscar=input("Por favor ingrese el código del libro que se está devolviendo: ")
    for libro in libros:
        if codigo_a_buscar==libro["cod"]:
            if libro["cant_ej_pr"]==libro["cant_ej_ad"]:
                print("Es imposible que se hayan prestado más libros de los que se adquirieron, por favor verifique el código ingresado")
            elif libro["cant_ej_pr"]==0:
                print("Hay un error, no fue prestado ningún libro con ese código, por favor verifique.")
            else:
                libro["cant_ej_pr"]-=1
                print(f"Con la presente devolución, los prestamos totales efectuados del código: {codigo_a_buscar} es de: ")
                print(libro["cant_ej_pr"])
                libro["cant_ej_ad"]+=1
                print(f"El stock de libros del código: {codigo_a_buscar} fue actualizado, ahora hay disponibles para prestar un total de: ")
                print(libro["cant_ej_ad"])
            return
    print(f"El código ingresado: {codigo_a_buscar} no se encuentra asignado a ningún libro existente, verifique.\n")
    return None

def nuevo_libro():
    #completar
    return None