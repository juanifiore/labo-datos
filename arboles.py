import csv

#%%

# EJERCICIO 1


'''
def leer_parque(nombre_archivo,parque):
    lista_arboles = []
    with open(nombre_archivo, 'rt') as file:
        filas = csv.reader(file)
        encabezado = next(filas)
        indice_columna_parque = encabezado.index('espacio_ve')
        for fila in filas:
            if fila[indice_columna_parque] == parque:
                lista_arboles.append(dict(zip(encabezado,fila)))
    return lista_arboles
'''


def leer_parque(nombre_archivo,parque): 
    lista_arboles = []
    with open(nombre_archivo, 'rt') as file:
        filas = csv.reader(file)        
        encabezado = next(filas)        # guardamos el encabezado
        indice_columna_parque = encabezado.index('espacio_ve')      #obtenemos indice de la columna que tiene el encabezado espacio_ve
        indice_columna_altura = encabezado.index('altura_tot')      #obtenemos indice de la columna que tiene el encabezado altura_tot
        for fila in filas:       #recorremos cada fila del archivo
            if fila[indice_columna_parque] == parque:       # buscamos los arboles ubicados en el parque indicado
                fila[indice_columna_altura] = float(fila[indice_columna_altura])      #modificamos el numero de la altura de string a float
                lista_arboles.append(dict(zip(encabezado,fila)))     #armamos el diccionario uniendo una clave del encabezado con su correspondiente valor usando la funcion zip, y eso lo agregamos al final de lista_arboles
    return lista_arboles


# EJERCICIO 2

def especies(lista_arboles):
    lista_especies = []
    for diccionario in lista_arboles:
        lista_especies.append(diccionario['nombre_com'])        # armamos una lista con los nombres de las especies de todos los arboles en la lista
    conjunto_especies = set(lista_especies)     # convertimos la lista en un conjunto
    return conjunto_especies


# EJERCICIO 3

def contar_ejemplares(lista_arboles):
    diccionario_ejemplares = {}
    especies_no_contadas = especies(lista_arboles)     # usamos la funcion especies() para armar un conjunto con todas las especies de la lista
    for diccionario in lista_arboles:
        especie_a_contar = diccionario['nombre_com']        # recorremos los diccionarios en la lista
        if diccionario['nombre_com'] in conjunto_especies:      # verificamos que la especie del arbol actual este en el conjunto
            contador = 0
            for diccionario_a_contar in lista_arboles:
                if diccionario_a_contar['nombre_com'] == especie_a_contar:      # volvemos a recorrer los diccionarios de la lista para contar las apariciones de la especie actual del ciclo
                    contador += 1
            conjunto_especies.remove(especie_a_contar)      # eliminamos la especie del conjunto para no volver a contarla
            diccionario_ejemplares[especie_a_contar] = contador        # añadimos el par clave-valor al diccionario que va a devolver la funcion, donde la clave es la especie y el valor la cantidad de ejemplares
    return diccionario_ejemplares


# EJERCICIO 4

def obtener_alturas(lista_arboles,especie):
    lista_alturas = []
    for diccionario in lista_arboles:
        if diccionario['nombre_com'] == especie:
            lista_alturas.append(diccionario['altura_tot'])         # recorremos los diccionarios de la lista y para los arboles de la especie indicada añadimos su altura a la lista
    return lista_alturas

# funcion para calcular altura maxima y promedio de una especie en un parque

def altura_promedio_y_maxima(lista_alturas):
    cantidad_arboles = len(lista_alturas)
    suma_alturas = 0
    for altura in lista_alturas:        #sumamos todas las alturas de la lista
        suma_alturas += altura      
    altura_promedio = suma_alturas/cantidad_arboles     #sacamos el promedio
    altura_maxima = 0
    for altura in lista_alturas:        #guardamos la altura maxima
        if altura > altura_maxima:
            altura_maxima = altura
    respuesta = {}      #armamos un diccionario con las respuestas
    respuesta['Altura promedio'] = altura_promedio
    respuesta['Altura maxima'] = altura_maxima

    return respuesta

# EJERCICIO 5

def obtener_inclinaciones(lista_arboles,especie):
    lista_inclinaciones = []
    for diccionario in lista_arboles:
        if diccionario['nombre_com'] == especie:        # recorremos los diccionarios de la lista y agregamos a la lista las inclinaciones de la especie indicada
            lista_inclinaciones.append(float(diccionario['inclinacio']))        #pasamos la inclinacion a float para poder usarla en el ejercicio 6
    return lista_inclinaciones


# EJERCICIO 6

def especimen_mas_inclinado(lista_arboles):
    especie_mas_inclinada = ''      # guardamos la especie con el ejemplar mas inclinado
    inclinacion_maxima = 0      # guardamos la inclinacion maxima
    especies_en_el_parque = especies(lista_arboles)     #obtenemos el conjunto de las especies 
    for especie in especies_en_el_parque:
        inclinaciones_especie = obtener_inclinaciones(lista_arboles,especie)        # recorremos las especies del conjunto y para cada especie armamos la lista con las inclinaciones de los arboles en el parque
        for inclinacion in inclinaciones_especie:
            if inclinacion > inclinacion_maxima:        # si encontramos una inclinacion superior a la inclinacion maxima anterior, guardamos esa inclinacion junto al nombre de la especie
                inclinacion_maxima = inclinacion
                especie_mas_inclinada = especie
    respuesta = {}      # armamos el diccionario con las respuestas
    respuesta['Especie mas inclinada'] = especie_mas_inclinada
    respuesta['Inclinacion'] = inclinacion_maxima
    return respuesta
        

# EJERCICIO 7


def especie_promedio_mas_inclinada(lista_arboles):
    especie_con_mayor_inclinacion_promedio = ''     # guardamos la especie con mayor inclinacion
    promedio_de_inclinacion_maximo = 0      # guardamos la mayor inclinacion promedio
    especies_en_el_parque = especies(lista_arboles)
    for especie in especies_en_el_parque:
        inclinaciones_especie = obtener_inclinaciones(lista_arboles,especie)        # recorremos las especies que hay en el parque y armamos la lista con sus inclinaciones
        cantidad_ejemplares = len(inclinaciones_especie)
        suma_inclinaciones = 0
        for inclinacion in inclinaciones_especie:       # hacemos la suma total de las inclinaciones de la especie
            suma_inclinaciones += inclinacion       
        promedio_inclinacion = suma_inclinaciones/cantidad_ejemplares       # sacamos el promedio de inclinacion de la especie
        if promedio_inclinacion > promedio_de_inclinacion_maximo:       # si el promedio es mayor al maximo ya guardado, lo cambiamos por el actual junto al nombre de la especie actual
            especie_con_mayor_inclinacion_promedio = especie
            promedio_de_inclinacion_maximo = promedio_inclinacion
    respuesta = {}      # armamos el diccionario con las respuestas
    respuesta['Especie con inclinacion promedio maxima'] = especie_con_mayor_inclinacion_promedio
    respuesta['Inclinacion promedio'] = promedio_de_inclinacion_maximo 
    return respuesta

#%%

# TEST DE FUNCIONES

# EJERCICIO 1
print('EJERCICIO 1')

print('La funcion en el parque General Paz debe devolver una lista de 690 diccionarios:')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','GENERAL PAZ')
print('Longitud de la lista de arboles en Gral Paz: ',len(lista_arboles))

print('\n \n')



# EJERCICIO 2
print('EJERCICIO 2')

print('Probamos la funcion pidiendo el conjunto de las especies en el parque Monte Castro:')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','MONTE CASTRO') 
especies_centenario = especies(lista_arboles)
print(especies_centenario)

print('\n \n')



# EJERCICIO 3
print('EJERCICIO 3')

print('Cantidad de Jacarandas en General Paz: (esperado 20)')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','GENERAL PAZ') 
diccionario_ejemplares = contar_ejemplares(lista_arboles)
print(diccionario_ejemplares['Jacarandá'])
print('\n')

print('Cantidad de Tilos en Parque los Andes: (esperado 3)')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','ANDES, LOS')
diccionario_ejemplares = contar_ejemplares(lista_arboles)
print(diccionario_ejemplares['Tilo'])
print('\n')

print('Cantidad de Laureles en Parque Centenario: (esperado 1)')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','CENTENARIO') 
diccionario_ejemplares = contar_ejemplares(lista_arboles)
print(diccionario_ejemplares['Laurel'])
print('\n \n')



# EJERCICIO 4
print('EJERCICIO 4')

print('Altura promedio y maxima del Jacarandá en el parque Gral Paz: (esperado 10.2 y 16.0)')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','GENERAL PAZ') 
lista_alturas = obtener_alturas(lista_arboles,'Jacarandá')
print(altura_promedio_y_maxima(lista_alturas))
print('\n')


print('Altura promedio y maxima del Jacarandá en el parque Los Andes: (esperado 10.54 y 25)')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','ANDES, LOS') 
lista_alturas = obtener_alturas(lista_arboles,'Jacarandá')
print(altura_promedio_y_maxima(lista_alturas))
print('\n')

print('Altura promedio y maxima del Jacarandá en el parque Centenario: (esperado 8.96 y 18)')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','CENTENARIO')
lista_alturas = obtener_alturas(lista_arboles,'Jacarandá')
print(altura_promedio_y_maxima(lista_alturas))
print('\n \n')



# EJERCICIO 5
print('EJERCICIO 5')

print('Lista de inclinaciones del Jacaranda en el parque Gral Paz:')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','GENERAL PAZ') 
print(obtener_inclinaciones(lista_arboles,'Jacarandá'))
print('\n \n')



# EJERCICIO 6
print('EJERCICIO 6')

print('La funcion deberia devolver que en el parque Centenario hay un Falso Guayabo inclinado 80 grados:')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','CENTENARIO')
print(especimen_mas_inclinado(lista_arboles))
print('\n \n')



# EJERCICIO 7
print('EJERCICIO 7')

print('La funcion debe devolver que los Álamos plateados del Parque Los Andes son la especie mas inclinada con un promedio de inclinacion de 25 grados:')
lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv','ANDES, LOS') 
print(especie_promedio_mas_inclinada(lista_arboles))
print('\n')
