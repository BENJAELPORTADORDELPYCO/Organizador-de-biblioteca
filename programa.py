from biblioteca import *
print("¡Saludos usuario!")
biblioteca = listaVacia
#programa :: biblioteca -> None
#Con una biblioteca, se pueden efectuar cambios a los libros, stocks, además de ordenar la biblioteca por distintos criterios.
#Permite consultar por prestamos y libros específicos, además de buscarlos por disntitos filtros.
def programa(biblioteca):
    print("Las funciones que puedes hacer son las siguientes:")
    print("1.Agregar o eliminar un libro de la biblioteca")
    print("2.Buscar un libro")
    print("3.Prestar o devolver un libro")
    print("4.Mostrar la cantidad de libros")
    print("5.Mostrar todos los libros")
    print("6.Ordenar los libros")
    print("7.Mostrar la editorial con más libros de la biblioteca")
    print("8.Salir")
    n = input("inserta un numero ")
    
    #1 Agregar o eliminar un libro a la biblioteca
    if n == "1":
        aoq = input("¿Deseas agregar o quitar un libro? ")
        if aoq == "agregar":
            isbn = int(input("¿ISBN? "))
            if isbnEnBiblio(isbn, biblioteca):
                print("Un libro con ese ISBN ya existe.")
                return programa(biblioteca)
            titulo = input("¿Título? ")
            autor = input("¿Autor? ")
            generourbano = input("¿Género? ")
            nedicion = int(input("¿Número de edición? "))
            añoedi = int(input("¿Año de edición? "))
            editorial = input("¿Editorial? ")
            return(programa(agregar_libro((crear_libro(isbn, titulo, autor, generourbano, nedicion, añoedi, editorial)), biblioteca)))
        
        elif aoq == "quitar":
            qlibro = int(input("¿Que libro quieres quitar?, inserta su isbn "))
            if not isbnEnBiblio(qlibro, biblioteca):
                print("No hay libro con ese ISBN.")
                return programa(biblioteca)
            return(programa(eliminar_libro(qlibro, biblioteca)))

    #2 Filtrar los libros según autor, año, rango de años, género, palabras específicas en el título, isbn,
    #disponibilidad o prestados a una persona en específico
    elif n == "2":
        t = input("¿Por que tipo de dato quieres filtrar? 1.autor 2.año de edición 3.rango de años de edición 4.género 5.palabra que contiene el título 6.ISBN 7.disponibles 8.prestados a una persona especifica 'prestados' ")
        #1
        if t == "1":
            qautor = input("Ingresa el autor ")
            libros_de_autor(biblioteca, qautor)
            return programa(biblioteca)
        
        #2
        elif t == "2":
            qaño = int(input("Ingresa el año "))
            libros_del_agno(biblioteca, qaño)
            return programa(biblioteca)

        #3
        elif t == "3":
            qdesde = int(input("Desde... "))
            qhasta = int(input("Hasta. "))
            libros_entre_agnos(biblioteca, qdesde, qhasta)
            return programa(biblioteca)
        
        #4
        elif t == "4":
            qgenero = input("Ingresa el género ")
            libros_por_genero(biblioteca, qgenero)
            return programa(biblioteca)
        
        #5
        elif t == "5":
            qpalabracont = input("Ingresa la palabra que contiene el título ")
            buscar_libros(biblioteca, qpalabracont)
            return programa(biblioteca)
        
        #6
        elif t == "6":
            qisbn = int(input("Ingresa el ISBN del libro "))
            if buscar_por_isbn(biblioteca, qisbn) == None:
                print("No existe")
                return programa(biblioteca)
            else:
                print(buscar_por_isbn(biblioteca, qisbn).titulo, buscar_por_isbn(biblioteca, qisbn).autor)
            return programa(biblioteca)
        
        #7
        elif t == "7":
            libros_disponibles(biblioteca)
            return programa(biblioteca)
        
        #8
        elif t == "8":
            persona = int(input("Ingresa el rut de la persona "))
            libros_prestados_persona(biblioteca, persona)
            return programa(biblioteca)
        
        else: return programa(biblioteca)
    #3 Prestar o devolver un libro
    if n == "3":
        pod = input("¿Quieres tomar prestado o devolver un libro? ")
        if pod == "tomar prestado":
            qprestar = int(input("Escribe el ISBN del libro que quieres tomar prestado "))
            stoc = buscar_stock(biblioteca, qprestar)
            if stoc == None:
                print("No hay libro con ese ISBN.")
                return programa(biblioteca)
            if stoc.estado == "prestado":
                print("En este momento no se puede prestar.")
                return programa(biblioteca)
            qrut = int(input("Ingresa tu rut "))
            qfecha = int(input("Ingresa la fecha de devolución. "))
            print("El libro ahora está prestado.")
            return programa(actualizar_biblioteca(biblioteca, prestar_libro(stoc, qrut, qfecha)))

        if pod == "devolver":
            qdevolver = int(input("Escribe el ISBN del libro que quieres devolver "))
            stoc = buscar_stock(biblioteca, qdevolver)
            if stoc == None:
                print("No hay libro con ese ISBN.")
                return programa(biblioteca)
            if stoc.estado == "disponible":
                print("Ese libro no estaba prestado.")
                return programa(biblioteca)
            print("Libro devuelto")
            return programa(actualizar_biblioteca(biblioteca, stock(stoc.libro, "disponible", None, None)))

        else:
            print("La opción ingresada no es válida") 
            return programa(biblioteca)
            
    #4 Mostrar la cantidad de libros totales que hay o la cantidad de disponibles
    if n == "4":
        qdispototal = input("¿La cantidad total o disponible? ingresar 'total' / 'disponible' ")
        if qdispototal == "total":
            print("Hay", contar_libros(biblioteca), "libros.")
            return programa(biblioteca)
        elif qdispototal == "disponible":
            print("Hay", contar_disponibles(biblioteca), "libros.")
            return programa(biblioteca)
        else: 
            return programa(biblioteca)
    #5 Mostrar todos los libros que hay en la biblioteca
    if n == "5":
        listar_biblioteca(biblioteca)
        return programa(biblioteca)
    #6 Ordenar los libros según año, título o autor
    if n == "6":
        qsegunq = input("Ingresa el parámetro para ordenar los libros 'año' / 'titulo' / 'autor' ")
        ascodesc = input("¿ascendente o descendente? ")
        if qsegunq == "año":
            if ascodesc == "ascendente":
                return(programa(ordenar_por_agno(biblioteca, "asc")))
            if ascodesc == "descendente":
                return(programa(ordenar_por_agno(biblioteca, "desc")))
            else: return programa(biblioteca)
        if qsegunq == "titulo":
            if ascodesc == "ascendente":
                return(programa(ordenar_por_titulo(biblioteca, "asc")))
            if ascodesc == "descendente":
                return(programa(ordenar_por_titulo(biblioteca, "desc")))
            else: return programa(biblioteca)
        if qsegunq == "autor":
            if ascodesc == "ascendente":
                return(programa(ordenar_por_autor(biblioteca, "asc")))
            if ascodesc == "descendente":
                return(programa(ordenar_por_autor(biblioteca, "desc")))
            else: return programa(biblioteca)
        else:
            return programa(biblioteca)

    #7 Mostrar la editorial con más libros en la biblioteca
    if n == "7":
        print("La editorial con mas libros en la biblioteca es:", editorial_mas_frecuente(biblioteca))
        return programa(biblioteca)
    #8 Salir
    if n == "8":
        print("Hasta la próxima")
        return None
    else:
        return programa(biblioteca)
programa(biblioteca)