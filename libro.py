# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

import cod_generator        # importo el programa que genera el código aleatorio

def nuevo_libro():
    # Damos de alta los datos para el nuevo ingreso de libros[], que cargo previamente en el diccionario
    nuevo_codigo=generar_codigo()                # Código del nuevo libro
    cant_nvo_libro=input("Por favor, indique la cantidad de libros que ingresan a la Biblioteca: ")
    cant_nuevo_libro=int(cant_nvo_libro)
    titulo_nuevo_libro=input("Título/Nombre del nuevo libro: ")
    autor_nuevo_libro=input("Autor/es del nuevo libro: ")
    confirma=""
    while confirma != "SI" and confirma != "NO":
        confirma=input("Confirma el alta del nuevo libro? (SI/NO):")
        if confirma=="SI":
            alta_nuevo_libro={"cod": nuevo_codigo, 
                              "cant_ej_ad": cant_nuevo_libro,
                              "cant_ej_pr": 0,
                              "titulo": titulo_nuevo_libro,
                              "autor": autor_nuevo_libro}
            print("\nSe ha dado de alta un nuevo registro con los siguientes datos:\n")
            print(f"Código: {nuevo_codigo}\nTítulo/Nombre del libro: {titulo_nuevo_libro}\nAutor/es: {autor_nuevo_libro}\nCantidad total: {cant_nuevo_libro}")
        elif confirma=="NO": 
            print("Se cancela el alta de un nuevo libro")
            alta_nuevo_libro={}
        else:
            print("Por favor, ingrese SI o NO")
    return alta_nuevo_libro

def generar_codigo():
    # Aquí se genera un código aleatorio con la función generar() dentro del programa cod_generator.py
    # Guardo el código generado en la función generar() en la variable cod
    nuevo_codigo=cod_generator.generar()
    return nuevo_codigo