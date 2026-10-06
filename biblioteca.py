from estructura import *
from lista import *
from libro import *

#stock : libro, estado(str), fechadev(int), rut(int)
crear("stock", "libro estado fechadev rut")

# ---------------------- libros para pruebas, ejemplos, etc. ----------------------
L1 = libro(9788420412146,  "El ingenioso hidalgo Don Quijote de la Mancha", "Miguel De Cervantes", "Novela Clásica", 1, 2015, "Alfaguara")
L2 = libro(9788466751698, "El ingenioso hidalgo Don Quijote de la Mancha", "Miguel De Cervantes", "Novela Clásica (Adaptada)", 2, 2006, "Anaya")
L3 = libro(9780307474728, "Cien años de soledad", "Gabriel Garcia Marquez", "Realismo Mágico", 1, 2009, "Vintage Español")
L4 = libro(9781101974193, "El amor en los tiempos de cólera", "Gabriel García Marquez", "Novela romántica", 1, 2015, "Vintage Español")
L5 = libro(9788415629146, "El código Da Vinci", "Dan Brown", "Suspenso / Misterio", 4, 2013, "Planeta" )
L6 = libro(9780000000006, "Los juegos del hambre", "Suzanne Collins", "Ciencia ficción", 1, 2009, "Molino")
# ---------------------- stocks para pruebas, ejemplos, etc. ----------------------
S1 = stock(L1, "disponible", None, None)
S2 = stock(L2, "prestado", 1304, 218857914)
S3 = stock(L3, "prestado", 2712, 130409709)
S4 = stock(L4, "disponible", None, None)
S5 = stock(L5, "prestado", 2001, 218857914) 
#---------------------- biblioteca para pruebas, ejemplos, etc. ----------------------
B0 = listaVacia
B1 = lista(S1, listaVacia)
B2 = lista(S2, listaVacia)
B3 = lista(S1, lista(S2, lista(S3, listaVacia)))
B5 = lista(S1, lista(S2, lista(S3, lista(S4, lista(S5, listaVacia))))) 
#----------------------                                         ----------------------
#isbnEnBiblio :: int biblioteca -> bool
#Dado isbn, chequea si un libro con mismo isbn se encuentra en la biblioteca
#ej: isbnEnBiblio(9788420412146, lista(S1, lista(S2, listavacia))) retorna True 
def isbnEnBiblio(isbn, biblioteca):
     assert (type(isbn) == int and esLista(biblioteca))
     if biblioteca == listavacia:
          return False
     if cabeza(biblioteca).libro.isbn == isbn:
          return True
     return isbnEnBiblio(isbn, biblioteca.siguiente)
assert isbnEnBiblio(9788420412146, lista(S1, lista(S2, listaVacia))) == True
assert isbnEnBiblio(123123, lista(S3, listaVacia)) == False

#agregar_libros :: lista -> lista
#agrega stocks a una biblioteca, si un libro con mismo isbn ya está, no agrega su stock.
#ej: agregar_libro(L6, B0) retorna lista(stock(L6, "disponible", None, None), listaVacia)
def agregar_libro(libro, biblioteca):
    assert esLista(biblioteca)
    if biblioteca == listaVacia:
        return insertar(stock(libro, "disponible", None, None), biblioteca)
    if isbnEnBiblio(libro.isbn, biblioteca):
        return biblioteca
    return insertar(stock(libro, "disponible", None, None), biblioteca)
assert agregar_libro(L6, B1) == lista(stock(L6, "disponible", None, None), B1)
assert agregar_libro(L1, B3) == B3
assert agregar_libro(L6, B0) == lista(stock(L6, "disponible", None, None), listaVacia)

#eliminar_libro :: int biblioteca -> biblioteca
#dado isbn y biblioteca, elimina el libro asociado al isbn de esta biblioteca.
#ej: eliminar_libro(L1.isbn, B1) retorna listaVacia
def eliminar_libro(isbn, biblioteca):
    assert (type(isbn) == int and esLista(biblioteca))
    if biblioteca == listavacia:
        return biblioteca
    if cabeza(biblioteca).libro.isbn == isbn:
        return eliminar_libro(isbn, cola(biblioteca))
    return lista(cabeza(biblioteca), eliminar_libro(isbn, cola(biblioteca)))
assert eliminar_libro(L1.isbn, B1) == listaVacia
assert eliminar_libro(L1.isbn, B3) == lista(S2, lista(S3, listaVacia))

#libros_de_autor :: biblioteca str -> None
#Muestra en pantalla los libros (titulo y autor) de dado autor en dada biblioteca
#ej: libros_de_autor(B5, "Dan Brown") muestra en pantalla "El codigo Da Vinci"
def libros_de_autor(biblioteca, autor):
    assert (esLista(biblioteca) and type(autor) == str)
    if biblioteca == listavacia:
        return print(" ")
    if cabeza(biblioteca).libro.autor == autor:
        print(cabeza(biblioteca).libro.titulo, " ")
    return libros_de_autor(cola(biblioteca), autor)

#buscar_libros :: biblioteca str -> None
#Muestra en pantalla los libros (titulo y autor) cuyo titulo contiene la palabra
#ej: buscar_libros(B5, "soledad") muestra en pantalla "Cien años de soledad Gabriel García Márquez"
def buscar_libros(biblioteca, palabra):
    assert (esLista(biblioteca) and type(palabra) == str)
    if biblioteca == listavacia:
        return print(" ")
    if contiene(cabeza(biblioteca).libro, palabra):
        print(cabeza(biblioteca).libro.titulo, cabeza(biblioteca).libro.autor, " ")
    return buscar_libros(cola(biblioteca), palabra)

#libros_del_agno :: biblioteca int -> None
#Muestra los libros (titulo y autor) editados en dado año
#ej: libros_del_agno(B5, 2015) muestra en pantalla "El ingenioso hidalgo Don Quijote de la Mancha Miguel De Cervantes"
# "El amor en los tiempos de cólera Gabriel García Marquez"
def libros_del_agno(biblioteca, agno):
    assert (esLista(biblioteca) and type(agno) == int)
    if biblioteca == listavacia:
        return print(" ")
    if cabeza(biblioteca).libro.año == agno:
        print(cabeza(biblioteca).libro.titulo, " ")
    return libros_del_agno(cola(biblioteca), agno)

#libros_entre_agnos :: biblioteca int int -> None
#Muestra en pantalla los libros (titulo y autor) editados entre dos años, incluyendo los años. 
#ej: libros_entre_agnos(B5, 2009, 2013) muestra en pantalla "Cien años de soledad Gabriel García Marquez"
#"El código Da Vinci Dan Brown"
def libros_entre_agnos(biblioteca, desde, hasta):
    assert (esLista(biblioteca) and type(desde) == int and hasta == int)
    if biblioteca == listavacia:
        return print(" ")
    if desde <= cabeza(biblioteca).libro.año <= hasta:
        print(cabeza(biblioteca).libro.titulo, cabeza(biblioteca).libro.autor, " ")
    return libros_entre_agnos(cola(biblioteca), desde, hasta)

#libros_por_genero :: biblioteca str -> None
#Muestra en pantalla la lista de libros cuyo género contiene el genero dado.
#ej: libros_por_genero(B5, "Novela") muestra en pantalla "El ingenioso hidalgo Don Quijote de la Mancha Miguel De Cervantes"
#"El ingenioso hidalgo Don Quijote de la Mancha Miguel De Cervantes"
#"El amor en los tiempos de cólera Gabriel García Márquez"
def libros_por_genero(biblioteca, genero):
    assert esLista(biblioteca) and type(genero) == str
    if biblioteca == listavacia:
        return print(" ")
    if genero in cabeza(biblioteca).libro.genero:
        print(cabeza(biblioteca).libro, " ")
    return libros_por_genero(cola(biblioteca), genero)

#libros_disponibles :: biblioteca -> None
#Muestra en pantalla los libros (titulo y autor) disponibles en dada biblioteca
#ej: libros_disponibles(B1) muestra en pantalla "El ingenioso hidalgo Don Quijote de la Mancha Miguel De Cervantes"
def libros_disponibles(biblioteca):
    assert esLista(biblioteca)
    if biblioteca == listavacia:
        return print(" ")
    if cabeza(biblioteca).estado == "disponible":
        print(cabeza(biblioteca).libro.titulo, cabeza(biblioteca).libro.autor)
    return libros_disponibles(cola(biblioteca))

#libros_prestados :: biblitoeca -> None
#Muestra en pantalla los libros prestados, viendo el rut de quien lo tiene, y la fecha de cuando lo devuelve
#ej: libros_prestados(B2) muestra en pantalla "El ingenioso hidalgo Don Quijote de la Mancha Miguel De Cervantes lo tiene 218857914 y lo devuelve el dia 1304" 
def libros_prestados(biblioteca):
    assert esLista(biblioteca)
    if biblioteca == listavacia:
        return print(" ")
    if cabeza(biblioteca).estado == "prestado":
        print(cabeza(biblioteca).libro.titulo, cabeza(biblioteca).libro.autor, \
                "lo tiene:", cabeza(biblioteca).rut, \
                    "y lo devuelve el dia", cabeza(biblioteca).fechadev)
    return libros_prestados(cola(biblioteca))

#libros_prestados_persona :: biblioteca rut(int) -> None
#Dada persona y biblioteca, muestra en pantalla los libros (titulo y autor) que tenga la persona
#ej: libros_prestados_persona(B5, 218857914) muestra en pantalla los libros de S2 y S5
def libros_prestados_persona(biblioteca, rut):
    assert (esLista(biblioteca) and type(rut) == int)
    if biblioteca == listavacia:
        return print(" ")
    if cabeza(biblioteca).rut == rut:
        print(cabeza(biblioteca).libro.titulo, cabeza(biblioteca).libro.autor, "lo devuelve el dia", cabeza(biblioteca).fechadev)
    return libros_prestados_persona(cola(biblioteca), rut)

#listar_biblioteca :: lista -> None
#Imprime los libros en forma de tabla.
def listar_biblioteca(biblioteca, contador=0):
    assert esLista(biblioteca)
    if contador == 0:
        print("ISBN | Título | Autor | Género | Edición | Año de edición | Editorial | Estado | Fecha devolución | Rut")
    if biblioteca == listaVacia:
        return print(" ")
    stoc = cabeza(biblioteca)
    lib = stoc.libro
    if stoc.estado == "prestado":
        print(lib.isbn, '|', lib.titulo, '|', lib.autor, '|', lib.genero, '|', lib.edicion, '|', lib.año, '|', lib.editorial, '|', stoc.estado, '|', stoc.fechadev, '|', stoc.rut)
    else:
        print(lib.isbn, '|', lib.titulo, '|', lib.autor, '|', lib.genero, '|', lib.edicion, '|', lib.año, '|', lib.editorial, '|', stoc.estado, '|', '-', '|', '-')
    return listar_biblioteca(cola(biblioteca), contador + 1)

#buscar_por_isbn :: biblioteca int -> libro / None
#Retorna el libro con el isbn indicado, o None si no existe
#ej: buscar_por_isbn(B5, L3.isbn) retorna L3
def buscar_por_isbn(L, isbn):
    assert (esLista(L) and type(isbn) == int)
    if L == listaVacia:
        return None
    if cabeza(L).libro.isbn == isbn:
        return cabeza(L).libro
    return buscar_por_isbn(cola(L), isbn)
assert buscar_por_isbn(B5, L3.isbn) == L3
assert buscar_por_isbn(B0, L1.isbn) == None

#auxiliar
#valor_campo :: stock str -> int | str
#Dado un stock y el dato ("agno", "titulo" o "autor"), retorna el valor por el que se ordena
#ej: valor_campo(S3, "agno") retorna 2009
def valor_dato(stoc, dato):
    assert dato == "agno" or dato == "titulo" or dato == "autor"
    if dato == "agno":
        return stoc.libro.año
    if dato == "titulo":
        return stoc.libro.titulo
    return stoc.libro.autor
assert valor_dato(S3, "agno") == 2009
assert valor_dato(S3, "titulo") == "Cien años de soledad"
assert valor_dato(S3, "autor") == "Gabriel Garcia Marquez"

#auxiliar
#insertarOrd :: stock lista str str -> lista
#En una lista previamente ordenada, inserta el elemento x en su lugar según el tipo de dato que se quiera ordenar y el orden dado
#ej: insertarOrd(S1, lista(S2, lista(S3, listaVacia)), "agno", "asc")
#retorna lista(S2, lista(S3, lista(S1, listaVacia)))
def insertarOrd(x, L, dato, ord):
    assert (esLista(L) and (dato == "agno" or dato == "titulo" or dato == "autor") and (ord == "asc" or ord == "desc"))
    if L == listaVacia:
        return lista(x, listaVacia)
    if ord == "asc":
        if valor_dato(x, dato) <= valor_dato(cabeza(L), dato):
            return lista(x, L)
        return lista(cabeza(L), insertarOrd(x, cola(L), dato, ord))
    if ord == "desc":
        if valor_dato(x, dato) >= valor_dato(cabeza(L), dato):
            return lista(x, L)
        return lista(cabeza(L), insertarOrd(x, cola(L), dato, ord))
assert insertarOrd(S1, listaVacia, "agno", "asc") == lista(S1, listaVacia)
assert insertarOrd(S1, lista(S2, lista(S3, listaVacia)), "agno", "asc") == lista(S2, lista(S3, lista(S1, listaVacia)))
assert insertarOrd(S1, lista(S2, lista(S3, listaVacia)), "agno", "desc") == lista(S1, lista(S2, lista(S3, listaVacia)))

#ordenar_por :: lista str str -> lista
#Esta es la función madre de ordenar por año, por titulo y por autor!!!
#Ordena la biblioteca según dato (agno, titulo, autor), en orden ascendente o descendente
#ej: ordenar_por(B5, "agno", "asc") retorna lista(S2, lista(S3, lista(S5, lista(S1, lista(S4, listaVacia)))))
def ordenar_por(L, dato, ord):
    assert (esLista(L) and (ord == "asc" or ord == "desc") and (dato == "agno" or dato == "titulo" or dato == "autor"))
    if L == listaVacia:
        return listaVacia
    return insertarOrd(cabeza(L), ordenar_por(cola(L), dato, ord), dato, ord)
assert ordenar_por(B5, "agno", "asc") == lista(S2, lista(S3, lista(S5, lista(S1, lista(S4, listaVacia)))))
assert ordenar_por(B5, "agno", "desc") == lista(S1, lista(S4, lista(S5, lista(S3, lista(S2, listaVacia)))))
assert ordenar_por(B5, "titulo", "desc") == lista(S1, lista(S2, lista(S5, lista(S4, lista(S3, listaVacia)))))
assert ordenar_por(B0, "agno", "asc") == listaVacia

### subfunciones de ordenar_por para datos especificos
def ordenar_por_agno(biblioteca, orden):
    return ordenar_por(biblioteca, "agno", orden)

def ordenar_por_titulo(biblioteca, orden):
    return ordenar_por(biblioteca, "titulo", orden)

def ordenar_por_autor(biblioteca, orden):
    return ordenar_por(biblioteca, "autor", orden)
###
#contarEditorial :: lista str -> int
#cuenta cuantos libros de cierta biblioteca son de cierta editorial
#ej: contarEditorial(B5, "Vintage Español") retorna 2
def contarEditorial(L, ed):
    assert (esLista(L) and type(ed) == str)
    if L == listaVacia:
        return 0
    if cabeza(L).libro.editorial == ed:
        return 1 + contarEditorial(cola(L), ed)
    return contarEditorial(cola(L), ed)
assert contarEditorial(B5, "Vintage Español") == 2

#editorial_mas_frecuente :: lista -> str
#Dada biblioteca, retorna la editorial que aparece con más frecuencia,
#en el caso de tener mas de una ganadora retorna la primera que mas tiene
#ej: editorial_mas_frecuente(B5) retorna "Vintage Español"
def editorial_mas_frecuente(L, mast=None):
    assert esLista(L)
    if L == listaVacia:
        return "Ninguna"
    if mast == None:
        mast = L
    opcion1 = cabeza(L).libro.editorial
    if cola(L) == listaVacia:
        return opcion1
    opcion2 = editorial_mas_frecuente(cola(L), mast)
    if contarEditorial(mast, opcion2) > contarEditorial(mast, opcion1):
        return opcion2
    return opcion1
assert editorial_mas_frecuente(B5) == "Vintage Español"
assert editorial_mas_frecuente(B0) == "Ninguna"
assert editorial_mas_frecuente(B1) == "Alfaguara"

#contar_disponibles :: lista -> int
#cuenta la cantidad de libros disponibles para prestar
#ej: contar_disponibles(B5) retorna 2
def contar_disponibles(L, total=0):
    assert esLista(L)
    if L == listaVacia:
        return total
    if cabeza(L).estado == "disponible":
        return contar_disponibles(cola(L), total+1)
    return contar_disponibles(cola(L), total)
assert contar_disponibles(B0) == 0
assert contar_disponibles(B1) == 1

#contar_libros :: lista -> int
#cuenta cuantos libros hay en una biblioteca
#ej: contar_libros(B5) retorna 5
def contar_libros(L):
    assert esLista(L)
    if L == listaVacia:
        return 0
    return 1 + contar_libros(cola(L))
assert contar_libros(B0) == 0
assert contar_libros(B1) == 1

#prestar_libro :: stock int int -> stock
#retorna un stock prestado con el rut y la fecha de devolucion
#ej: prestar_libro(S1, 111, 1010) retorna stock(L1, "prestado", 1010, 111)
def prestar_libro(stoc, rut, fecha):
    assert ((type(rut) == int) and type(fecha) == int)
    if stoc.estado == "prestado":
        print("No se puede prestar actualmente")
        return stoc
    if stoc.estado == "disponible":
        return stock(stoc.libro, "prestado", fecha, rut)
assert prestar_libro(S1, 111, 1010) == stock(L1, "prestado", 1010, 111)
assert prestar_libro(S4, 222, 2020) == stock(L4, "prestado", 2020, 222)
assert S1 == stock(L1, "disponible", None, None)

#actualizar_biblioteca :: lista stock -> lista
#En la biblioteca, busca hasta encontrar el libro del stock (mismo isbn) y reemplaza su stock
#ej: actualizar_biblioteca(B1, stock(L1, "prestado", 1010, 111)) retorna lista(stock(L1, "prestado", 1010, 111), listaVacia)
def actualizar_biblioteca(L, stoc):
    assert esLista(L)
    if L == listaVacia:
        return listaVacia
    if cabeza(L).libro.isbn == stoc.libro.isbn:
        return lista(stoc, cola(L))
    return lista(cabeza(L), actualizar_biblioteca(cola(L), stoc))
prest = stock(L1, "prestado", 1010, 111)
disp = stock(L3, "disponible", None, None)
assert actualizar_biblioteca(B1, prest) == lista(prest, listaVacia)
assert actualizar_biblioteca(B3, prest) == lista(prest, lista(S2, lista(S3, listaVacia)))

#auxiliares para programa.py!!!

#buscar_stock :: lista int -> stock | None
#dado isbn, retorna el stock. es complemento de buscar_libro
#ej: buscar_stock(B5, L2.isbn) retorna S2
def buscar_stock(L, isbn):
    assert (esLista(L) and type(isbn) == int)
    if L == listaVacia:
        return None
    if cabeza(L).libro.isbn == isbn:
        return cabeza(L)
    return buscar_stock(cola(L), isbn)
assert buscar_stock(B5, L2.isbn) == S2
assert buscar_stock(B5, L6.isbn) == None

