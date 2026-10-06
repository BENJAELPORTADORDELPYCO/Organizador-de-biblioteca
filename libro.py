from estructura import *
from lista import *
#libro : isbn(int), titulo(str), autor(str), genero(str), edicion(int), año(int), editorial(str)
crear("libro", "isbn titulo autor genero edicion año editorial")
# ---------------------- libros para pruebas, ejemplos, etc. ----------------------
L1 = libro(9788420412146,  "El ingenioso hidalgo Don Quijote de la Mancha", "Miguel De Cervantes", "Novela Clásica", 1, 2015, "Alfaguara")
L2 = libro(9788466751698, "El ingenioso hidalgo Don Quijote de la Mancha", "Miguel De Cervantes", "Novela Clásica (Adaptada)", 2, 2006, "Anaya")
L3 =  libro(9780307474728, "Cien años de soledad", "Gabriel Garcia Marquez", "Realismo Mágico", 1, 2009, "Vintage Español")
L4 = libro(9781101974193, "El amor en los tiempos de cólera", "Gabriel García Marquez", "Novela romántica", 1, 2015, "Vintage Español")
L5 = libro(9788415629146, "El código Da Vinci", "Dan Brown", "Suspenso / Misterio", 4, 2013, "Planeta" )

#crear_libros :: int str str str int int str -> libro 
#A partir de dadas caracteristicas de un libro(isbn, titulo, autor, genero, n de edicion, año de edicion, editorial), crea un libro con estas caracteristicas
#ej: crear_libro(9791323567123, El ingenioso hidalgo don Quixote de la Mancha, Cervantes, novela, 1, 1605, principe) retorna
#libro(9791323567123, El ingenioso hidalgo don Quixote de la Mancha, Cervantes, novela, 1, 1605, principe)
def crear_libro(isbn, titulo, autor, genero, nro_edicion, agno_edicion, editorial):
    assert type(isbn) == int and type(titulo) == str and type(autor) == str and type(genero) == str and type(nro_edicion) == int \
    and type(agno_edicion) == int and type(editorial) == str
    return libro(isbn, titulo, autor, genero, nro_edicion, agno_edicion, editorial)
assert crear_libro(123123, "Las lombrices", "Benjamín Pérez", "Terror Psicológico", 1, 2026, "Planeta") == libro(123123, "Las lombrices", "Benjamín Pérez", "Terror Psicológico", 1, 2026, "Planeta")

#get_ISBN :: libro(int) -> int
#Dado un libro, extrae su ISBN
#ej:libro(L1) retorna 9788420412146
def get_ISBN(libro):
    return libro.isbn
assert get_ISBN(L1) == 9788420412146

#contiene :: libro(titulo) str -> bool
#Dado libro y palabra Retorna True en caso de contener la palabra en el título 
#ej: contiene(L1, "Quijote") retorna True
def contiene(libro, palabra):
    if palabra in libro.titulo:
        return True
    else:
        return False
assert contiene(L1, "Quijote")
assert not contiene(L5, "Hidalgo")

#mismo_libro :: libro libro -> bool
#Dados dos libros, identifica si es que son el mismo titulo del mismo autor, en el caso retorna True
#ej: mismo_libro(L1, L3) retorna False
def mismo_libro(libro1, libro2):
    if libro1.autor == libro2.autor and libro1.titulo == libro2.titulo:
        return True
    return False
assert not mismo_libro(L1, L3)
assert mismo_libro(L1, L1)
