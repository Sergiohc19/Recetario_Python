import os.path
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "C:\\Users\\Sergio\\OneDrive\\Escritorio\\DEVELOPER\\Recetas")

def contador_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

def inicio ():
    system("cls")
    saludo = input("Hola , ¿Cómo te llamas? ")
    print('*' * 50)
    print('*' * 5 + f" Hola {saludo}. Bienvenido al Recetario " + '*' * 5)
    print('*' * 50)
    print(f"Aquí están tus recetas: {mi_ruta}")
    print(f"Tienes un total de  {contador_recetas(mi_ruta)} recetas")

    elecion_menu = "x"
    while not elecion_menu.isnumeric() or int(elecion_menu) not in range(1,7):
        print("Elige una opción: ")
        print("""
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa
        """)
        elecion_menu = input()
    return int(elecion_menu)

def mostrar_categorías(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - [{carpeta_str}]")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = "x"
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoría: ")

    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - [{receta_str}]")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista), 1):
        eleccion_receta = input("\nElige una receta: ")

    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path(receta).read_text())

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.read_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoría: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoría ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"la categoria {categoria.name} ha sido eliminada")

def volver_al_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower != "V":
        eleccion_regresar = input("\nPresione V para volver al menu: ")

finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorías(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas =  mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_al_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorías(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_al_inicio()

    elif menu == 3:
        mis_categorias = mostrar_categorías(mi_ruta)
        crear_categoria(mi_ruta)
        volver_al_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorías(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_al_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categorías(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_al_inicio()

    elif menu == 6:
        finalizar_programa = True



















