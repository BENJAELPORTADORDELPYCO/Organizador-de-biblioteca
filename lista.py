import estructura

### Módulo lista con funciones nuevas ###

#lista :: valor(any), siguiente(lista)
estructura.crear("lista", "valor siguiente")
listaVacia = None
listavacia = None
listax = lista(3, lista(29, lista( 12, listaVacia)))

#esLista :: lista -> bool
#verifica que la lista dada adhiera con la definicion
#de la estructura
#ejemplo: esLista(lista(1,lista(2,lista(3,listaVacia)))) devuelve True
#ejemplo 2: esLista(listaVacia) devuelve True
def esLista(L):
    if L == listaVacia:
        return True
    return type(L) == lista and esLista(L.siguiente)
assert esLista(lista(1,lista(2,lista(3,listaVacia))))
assert esLista(listaVacia)

#insertar :: any lista -> lista
#inserta el elemento x al principio de la lista L
#ejemplo: insertar(1, listaVacia) devueve lista(1,listaVacia)
#ejemplo: insertar(0, lista(1,lista(2,lista(3,listaVacia))))
#devuelve lista(0,lista(1,lista(2,lista(3,listaVacia))))
def insertar(x,L):
    assert esLista(L)
    if L == listaVacia:
        return lista(x,listaVacia)
    return lista(x,L)
assert insertar(1,listaVacia) == lista(1,listaVacia)
assert insertar(0,lista(1,lista(2,lista(3,listaVacia)))) == lista(0,lista(1,lista(2,lista(3,listaVacia))))

#cabeza :: lista -> any
#devuelve el valor del primer nodo de la lista L
#ejemplo: cabeza(lista(47,lista(38,lista(25,lista(19,lista(7,listaVacia))))))
#devuelve 47
def cabeza(L):
    if L == listaVacia:
        return None
    return L.valor
assert cabeza(listaVacia) == None
assert cabeza(lista(47, lista(38, lista(25, lista(19, lista(7, listaVacia)))))) == 47

#cola :: lista -> lista
#devuelve lo que viene a continuacion del primer
#nodo de la lista L
#ejemplo: cola(lista(47,lista(38,lista(25,lista(19,lista(7,listaVacia)))))
#devuelve lista(38,lista(25,lista(19,lista(7,listaVacia))))
def cola(L):
    assert esLista(L)
    if L == listaVacia:
        return listaVacia
    return L.siguiente
assert cola(listaVacia) == listaVacia
assert cola(lista(47,lista(38,lista(25,lista(19,lista(7,listaVacia)))))) == lista(38,lista(25,lista(19,lista(7,listaVacia))))

#largo :: lista -> int
#devuelve el numero de elementos que hay en L
#ejemplo: largo(lista(47,lista(38,lista(25,lista(19,lista(7,listaVacia)))))) devuelve 5
def largo(L):
    assert esLista(L)
    if L == listaVacia:
        return 0
    return 1 + largo(cola(L))
assert largo(listaVacia) == 0
assert largo(lista(47,lista(38,lista(25,lista(19,lista(7,listaVacia)))))) == 5

#suma :: lista(int) -> int
#devuelve la suma de los valores en una lista
#DE ENTEROS L
def suma(L):
    assert esLista(L)
    if L == listaVacia:
        return 0
    return cabeza(L) + suma(cola(L))
assert suma(listaVacia) == 0
assert suma(lista(47,lista(38,lista(25,lista(19,lista(7,listaVacia)))))) == 136

#listaPares :: lista(int+) -> lista
#devuelve la lista con los valores pares en una lista L
#ejemplo: listaPares(lista(47,lista(38,lista(25,lista(20,lista(7,listaVacia))))))
#devuelve lista(38,lista(20,listaVacia))
def listaPares(L):
    assert esLista(L)
    #propuesto: verificar que todos sean int >= 0
    if L == listaVacia:
        return listaVacia
    if cabeza(L) % 2 == 0:
        return lista(cabeza(L),listaPares(cola(L)))
    else:
        return listaPares(cola(L))
assert listaPares(listaVacia) == listaVacia
assert listaPares(lista(47,lista(38,lista(25,lista(20,lista(7,listaVacia)))))) == lista(38,lista(20,listaVacia))
assert listaPares(lista(1,lista(3,lista(5,listaVacia)))) == listaVacia
assert listaPares(lista(2,lista(4,lista(6,listaVacia)))) == lista(2,lista(4,lista(6,listaVacia)))

#enLista :: lista any -> bool
#Revisa si x se encuentra en la lista l y retorna un booleano
#ej: enLista(3, listax) retorna True 
def enLista(x, l):
    if l == listaVacia:
        return False
    if cabeza(l) == x:
        return True
    return enLista(x, cola(l))
assert enLista(3, listax) 
assert not enLista(2, listax)

def elimdeLista(x, l):
    if l == listavacia:
        return l
    if cabeza(l) == x:
        return elimdeLista(x, cola(l))
    return lista(cabeza(l), elimdeLista(x,cola(l)))

