import os
import graphviz

peliculas = [
{'Nombre': 'The Avengers', 'Actores': ['Robert Downey Jr', 'Chris Evans', 'Chris Hemsworth'], 'Año': 2012, 'Género': 'Ficcion'},
{'Nombre': 'Spiderman', 'Actores': ['Tobey Maguire', 'Kirsten Dunst', 'Willem Dafoe'], 'Año': 2002, 'Género': 'Accion'},
{'Nombre': 'The Amazing Spiderman', 'Actores': ['Andrew Garfield', 'Emma Stone'], 'Año': 2012, 'Género': 'Accion'},
{'Nombre': 'The Amazing Spiderman 2', 'Actores': ['Andrew Garfield', 'Emma Stone'], 'Año': 2014, 'Género': 'Accion'},
{'Nombre': 'Spiderman Homecoming', 'Actores': ['Tom Holland', 'Zendaya'], 'Año': 2017, 'Género': 'Accion'},
{'Nombre': 'Avengers Infinity War', 'Actores': ['Robert Downey Jr', 'Tom Holland'], 'Año': 2018, 'Género': 'Accion'}
]

peliculas = []
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def main_menu():
    global peliculas
    clear_console()
    print("***** Bienvenido al menú *****")
    print("1. Cargar archivo de entrada")
    print("2. Gestionar peliculas")
    print("3. Filtrado")
    print("4. Grafica")
    print("5. Salir")
    print("*********************")
    # Pedir al usuario que seleccione una opción
    choice = input("Selecciona una opción: ")    
    # Validar la opción seleccionada
    if choice == "1":
        opcion1()
    elif choice == "2":
        opcion2()
    elif choice == "3":
        opcion3()
    elif choice == "4":
        opcion4() 
    elif choice == "5":
        print("Saliendo...")
    else:
        print("Opción no válida")
        main_menu()
    input("Presiona cualquier tecla para continuar...")
    main_menu()
    #Realizar la primera funcion para la opción 1    
def opcion1():
    global peliculas
    clear_console()
    print("Seleccionaste la opción Cargar archivo de entrada")
    with open('datos.lfp', 'r') as f:
        lines = f.readlines()
    peliculas = []
    for line in lines:
        valores = line.strip().split(';')
        pelicula = {
            'Nombre': valores[0],
            'Actores': valores[1].split(','),
            'Año': int(valores[2]),
            'Género': valores[3]
        }
        peliculas.append(pelicula)
    peliculas_ordenadas = sorted(peliculas, key=lambda x: (x['Año'], x['Nombre']))
    for pelicula in peliculas_ordenadas:
        print('Nombre:', pelicula['Nombre'])
        print('Actores:', ', '.join(pelicula['Actores']))
        print('Año:', pelicula['Año'])
        print('Género:', pelicula['Género'])
        print()
    input("Presiona cualquier tecla para continuar...")
    main_menu()
# Realizar la segunda función para la opción 2
def opcion2():
    global peliculas
    clear_console()
    print("1. Información de todas las películas")
    print("2. Información de actores y películas")
    choice = input("Selecciona una opción: ")
    if choice == "1":
        clear_console()
        print("Mostrando información de todas las películas:")
        for pelicula in peliculas:
            print('Nombre:', pelicula['Nombre'])
            print('Actores:', ', '.join(pelicula['Actores']))
            print('Año:', pelicula['Año'])
            print('Género:', pelicula['Género'])
            print()
        input("Presiona cualquier tecla para continuar...")
        main_menu()
    elif choice == "2":
        clear_console()
        print("Mostrando información de actores y películas:")
        # Crear un diccionario de actores y películas
        actores_peliculas = {}
        for pelicula in peliculas:
            for actor in pelicula['Actores']:
                if actor not in actores_peliculas:
                    actores_peliculas[actor] = [pelicula['Nombre']]
                else:
                    actores_peliculas[actor].append(pelicula['Nombre'])
        # Mostrar la información de actores y películas
        for actor, peliculas in actores_peliculas.items():
            print(f"{actor}: {', '.join(peliculas)}")
        input("Presiona cualquier tecla para continuar...")
        main_menu()
    else:
        print("Opción no válida")
        input("Presiona cualquier tecla para continuar...")
        main_menu()
#Realizar la opcion 3  
def opcion3():

    input("Presiona cualquier tecla para continuar...l")
    main_menu()

def opcion4():
    clear_console()
    print("Selecionaste la opcion de Graficar")
    # Crear grafo
grafo = graphviz.Graph()

# Agregar nodos para películas
for pelicula in peliculas:
    grafo.node(pelicula['Nombre'], label=f"{pelicula['Nombre']}\n{pelicula['Año']}\n{pelicula['Género']}")

# Agregar nodos para actores
actores = set([actor for pelicula in peliculas for actor in pelicula['Actores']])
for actor in actores:
    grafo.node(actor, shape='oval')

# Agregar conexiones entre películas y actores
for pelicula in peliculas:
    for actor in pelicula['Actores']:
        grafo.edge(pelicula['Nombre'], actor)

# Generar grafo
grafo.view()
    #input("Presiona cualquier tecla para continuar...")
    #main_menu()

print("************************************************")
print("Nombre:  Frander Oveldo Carreto Gomez")
print("Carnet:  201901371")
print("Curso:   Lenguajes Formales")
print("Seccion: A-")
print("************************************************")
input("Presiona cualquier tecla para mostrar el menú...")

main_menu()