import psycopg2

def conectarse():
    connection = psycopg2.connect(user = "******",password = "******",host = "******",port = "******",database = "******")
    cursor = connection.cursor()
    return cursor    


def consultardb(xdb, cadena):
    xdb.execute(cadena)
    listaNombres = xdb.fetchall()      

    if listaNombres != []: 
        for nombre in listaNombres:
            return nombre 
    else:
        return None

def guardardb(xdb, cadena):
    xdb.execute(cadena)
    try:
        tabla = xdb.fetchall() 
        if tabla != []: 
            return tabla
    except:
        pass

def consultarvista(xdb, cadena):
    xdb.execute(cadena)
    listaNombres = xdb.fetchall()      

    if listaNombres != []: 
        return listaNombres 
    else:
        return None

def consultaestados(xdb, cadena):
    xdb.execute(cadena)
    listaNombres = xdb.fetchall()      

    if listaNombres != []: 
        return listaNombres 
    else:
        return None

def consultaparentesco(xdb, cadena):
    xdb.execute(cadena)
    listaNombres = xdb.fetchall()      

    if listaNombres != []: 
        return listaNombres 
    else:
        return None

def consultaidstud(xdb, cadena):
    xdb.execute(cadena)
    listaNombres = xdb.fetchall()      

    if listaNombres != []: 
        return listaNombres 
    else:
        return None

def actualizarinfo(xdb, cadena):
    xdb.execute(cadena)
    listaNombres = xdb.fetchall()      

    if listaNombres != []: 
        return listaNombres 
    else:
        return None
    
def cargarestudiantes(xdb, cadena):
    xdb.execute(cadena)
    listaNombres = xdb.fetchall()      

    if listaNombres != []: 
        for nombre in listaNombres:
            return listaNombres 
    else:
        return None