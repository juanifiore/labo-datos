'''
Guia sql, Laboratorio de datos
Tema dengue
Juan Igacio Fiore 259/22
INDICE:
    1: 30
    2: 320
    3: 445
    4: 490
'''

from inline_sql import sql
import pandas as pd
import os

def main():

    '''ARMO LOS CSV'''
    #ruta = '/home/juani/Documentos/Facultad/3 LABORATORIO DE DATOS/labo-datos/csv'
    ruta = './csv'
    casos = pd.read_csv(os.path.join(ruta,'casos.csv'))
    tipoevento = pd.read_csv(os.path.join(ruta,'tipoevento.csv'))
    departamento = pd.read_csv(os.path.join(ruta,'departamento.csv'))
    provincia = pd.read_csv(os.path.join(ruta,'provincia.csv'))
    grupoetario = pd.read_csv(os.path.join(ruta,'grupoetario.csv'))

    ''' ENTRADA PARA ELEGIR EJERCICIO A IMPRIMIR '''

    print('Inserte numero y letra de ejercicio')
    entrada = input()
    
    '''EJERCICIOS'''

#------------------------------------------------------------------

    if entrada == '1a':
        
        '''EJERCICIO 1A'''

        consigna = 'Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (dejando los registros repetidos).'

        consultaSQL = '''
                        SELECT descripcion
                        FROM departamento
                      
                      '''
        imprimirEjercicio(consigna,[departamento],consultaSQL)

#-------------------------------------------------------------------- 

    if entrada == '1b':

        '''EJERCICIO 1B'''

        consigna = 'Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (eliminando los registros repetidos).'

        consultaSQL = '''
                        SELECT DISTINCT descripcion
                        FROM departamento
                      '''
        
        imprimirEjercicio(consigna,[departamento],consultaSQL)

#---------------------------------------------------------------------------

    if entrada == '1c':

        '''EJERCICIO 1C'''

        consigna = 'Listar sólo los códigos de departamento y sus nombres de todos los departamentos que hay en la tabla departamento.'''

        consultaSQL = '''
                        SELECT id, descripcion
                        FROM departamento
                      '''

        imprimirEjercicio(consigna,[departamento],consultaSQL)
        
#--------------------------------------------------------------------------


    if entrada == '1d':

        '''EJERCICIO 1D'''

        consigna = 'Listar todas las columnas de departamento'

        consultaSQL = '''
                        SELECT * 
                        FROM departamento
                      '''

        imprimirEjercicio(consigna,[departamento],consultaSQL)

#-------------------------------------------------------------------------------


    if entrada == '1e':

        '''EJERCICIO 1E'''

        consigna = 'Listar los códigos de departamento y nombres de todos los departamentos que hay en la tabla departamento. Utilizar los siguientes alias para las columnas: codigo_depto, nombre_deptos'''

        consultaSQL = '''
                        SELECT id AS codigo_depto, descripcion AS nombre_deptos
                        FROM departamento
                      '''

        imprimirEjercicio(consigna,[departamento],consultaSQL)

#----------------------------------------------------------------------------------


    if entrada == '1f':

        '''EJERCICIO 1F'''

        consigna = 'Listar los códigos de departamento y sus nombres, ordenados por sus nombres de manera descendentes (de la Z a la A). En caso de empate, desempatar por código de departamento de manera ascendente.'''

        consultaSQL = '''
                        SELECT id, descripcion
                        FROM departamento
                        ORDER BY descripcion DESC, id DESC
                      '''

        imprimirEjercicio(consigna,[departamento],consultaSQL)

#---------------------------------------------------------------------------------

    if entrada == '1g':

        '''EJERCICIO 1G'''

        consigna = 'Listar los registros de la tabla departamento cuyo codigo de provincia es 54'

        consultaSQL = '''
                        SELECT DISTINCT descripcion, id_provincia
                        FROM departamento
                        WHERE id_provincia = '54'
                      '''

        imprimirEjercicio(consigna,[departamento],consultaSQL)


#---------------------------------------------------------------------------------

    if entrada == '1h':

        '''EJERCICIO 1H'''

        consigna = 'Listar los registros de la tabla departamento cuyo código de provincia es igual a 22, 78 u 86'

        consultaSQL = '''
                        SELECT descripcion, id_provincia
                        FROM departamento
                        WHERE id_provincia IN ('22','78','86')
                      '''

        imprimirEjercicio(consigna,[departamento],consultaSQL)



#---------------------------------------------------------------------------------



    if entrada == '1i':

        '''EJERCICIO 1I'''

        consigna = 'Listar los registros de la tabla departamento cuyos códigos de provincia se encuentren entre el 50 y el 59 (ambos valores inclusive).'

        consultaSQL = '''
                        SELECT descripcion, id_provincia
                        FROM departamento
                        WHERE id_provincia >= '50' AND id_provincia <= 59
                      '''

        imprimirEjercicio(consigna,[departamento, provincia],consultaSQL)



#---------------------------------------------------------------------------------



    if entrada == '1j':

        '''EJERCICIO 1J'''

        consigna = 'Listar los registros de la tabla provincia cuyos nombres comiencen con la letra M.'

        consultaSQL = '''
                        SELECT id, descripcion
                        FROM provincia
                        WHERE descripcion LIKE 'M%'
                      '''

        imprimirEjercicio(consigna,[provincia],consultaSQL)



#---------------------------------------------------------------------------------



    if entrada == '1k':

        '''EJERCICIO 1K'''

        consigna = 'Listar los registros de la tabla provincia cuyos nombres comiencen con la letra S y su quinta letra sea una letra A.'

        consultaSQL = '''
                        SELECT id, descripcion
                        FROM provincia
                        WHERE descripcion LIKE 'S___a%'
                      '''

        imprimirEjercicio(consigna,[provincia],consultaSQL)



#---------------------------------------------------------------------------------



    if entrada == '1l':

        '''EJERCICIO 1L'''

        consigna = 'Listar provincias que terminan con A'

        consultaSQL = '''
                        SELECT id, descripcion
                        FROM provincia
                        WHERE descripcion LIKE '%a'
                      '''

        imprimirEjercicio(consigna,[provincia],consultaSQL)



#---------------------------------------------------------------------------------



    if entrada == '1m':

        '''EJERCICIO 1M'''

        consigna = 'Provincias con 5 letras'

        consultaSQL = '''
                        SELECT id, descripcion
                        FROM provincia
                        WHERE descripcion LIKE '_____'
                      '''

        imprimirEjercicio(consigna,[provincia],consultaSQL)




#---------------------------------------------------------------------------------



    if entrada == '1n':

        '''EJERCICIO 1N'''

        consigna = 'Provincias que tengan do en alguna parte de su nombre'

        consultaSQL = '''
                        SELECT id, descripcion
                        FROM provincia
                        WHERE descripcion LIKE '%do%'
                      '''

        imprimirEjercicio(consigna,[provincia],consultaSQL)



#---------------------------------------------------------------------------------



    if entrada == '1o':

        '''EJERCICIO 1O'''

        consigna = 'Provincias que tengan do y su id sea menor a 30'

        consultaSQL = '''
                        SELECT id, descripcion
                        FROM provincia
                        WHERE descripcion LIKE '%do%' AND id < '30'
                      '''

        imprimirEjercicio(consigna,[provincia],consultaSQL)



#---------------------------------------------------------------------------------



    if entrada == '1p':

        '''EJERCICIO 1P'''

        consigna = 'Listar los registros de la tabla departamento cuyos nombres tengan ”san” en alguna parte de su nombre. Listar sólo id y descripcion. Utilizar los siguientes alias para las columnas: codigo_depto y nombre_depto, respectivamente. El resultado debe estar ordenado por sus nombres de manera descendentes (de la Z a la A).'

        consultaSQL = '''
                        SELECT id AS codigo_depto, descripcion AS nombre_depto
                        FROM departamento
                        WHERE nombre_depto LIKE '%pa%'
                        ORDER BY nombre_depto DESC
                      '''

        imprimirEjercicio(consigna,[departamento],consultaSQL)



#---------------------------------------------------------------------------------

# INNER JOIN

    if entrada == '2a':

        '''EJERCICIO 2A'''

        consigna = 'Devolver una lista con los código y nombres de departamentos, asociados al nombre de la provincia al que pertenecen'

        consultaSQL = '''
                        SELECT departamento.id , departamento.descripcion AS nombre_depto, provincia.descripcion AS provincia
                        FROM departamento
                        INNER JOIN provincia ON provincia.id = id_provincia
                      '''

        imprimirEjercicio(consigna,[departamento,provincia],consultaSQL)



#---------------------------------------------------------------------------------


    if entrada == '2b':

        '''EJERCICIO 2B'''

        consigna = 'Devolver una lista con los código y nombres de departamentos, asociados al nombre de la provincia al que pertenecen. Ordenar el resultado por nombre de provincia de manera ascendente, y dentro de cada una de ellas por nombre de departamento, también de manera ascendente.'

        consultaSQL = '''
                        SELECT departamento.id , departamento.descripcion AS nombre_depto, provincia.descripcion AS provincia
                        FROM departamento
                        INNER JOIN provincia ON provincia.id = id_provincia
                        ORDER BY provincia ASC, nombre_depto ASC 
                      '''

        imprimirEjercicio(consigna,[departamento,provincia],consultaSQL)



#---------------------------------------------------------------------------------


    if entrada == '2c':

        '''EJERCICIO 2C'''

        consigna = 'Devolver los casos de la provincia de Chaco'

        consultaSQL = '''
                        SELECT casos.*, provincia.descripcion AS provincia 
                        FROM casos, departamento, provincia
                        WHERE id_depto = departamento.id AND id_provincia = provincia.id AND provincia.descripcion = 'Chaco'
                      '''

        imprimirEjercicio(consigna,[casos,provincia],consultaSQL)



#---------------------------------------------------------------------------------


    if entrada == '2d':

        '''EJERCICIO 2D'''

        consigna = 'Devolver casos de BA cuyo campo cantidad supere los 10 casos'

        consultaSQL = '''
                        SELECT DISTINCT casos.*, provincia.descripcion AS provincia 
                        FROM casos, departamento, provincia
                        WHERE id_depto = departamento.id AND id_provincia = provincia.id AND provincia.descripcion = 'Buenos Aires' AND cantidad > '10'
                      '''

        imprimirEjercicio(consigna,[casos,provincia],consultaSQL)
            


#---------------------------------------------------------------------------------


    if entrada == '2e':

        '''EJERCICIO 2E'''

        consigna = 'Devolver aquellos casos de las provincias cuyo nombre terminen con la letra a y el campo cantidad supere 10. Mostrar: nombre de provincia, nombre de departamento, año, semana epidemiológica, descripción de grupo etario y cantidad. Ordenar el resultado por la cantidad (descendente), luego por el nombre de la provincia (ascendente), nombre del departamento (ascendente), año (ascendente) y la descripción del grupo etario (ascendente)'         

        consultaSQL = '''
                        SELECT provincia.descripcion AS provincia, departamento.descripcion AS depto, anio, semana_epidemiologica, grupoetario.descripcion AS grupoEtario, cantidad
                        FROM casos, departamento, provincia, grupoetario
                        WHERE id_grupoetario = grupoetario.id AND id_depto = departamento.id AND id_provincia = provincia.id AND provincia.descripcion LIKE '%a' AND cantidad > '10'
                        ORDER BY cantidad DESC, provincia ASC, departamento ASC, anio ASC, grupoEtario ASC
                      '''

        imprimirEjercicio(consigna,[casos,provincia],consultaSQL)





#---------------------------------------------------------------------------------


    if entrada == '2f':

        '''EJERCICIO 2F'''

        consigna = 'Idem anterior pero solo aquellas tuplas que tengan el maximo en el campo cantidad'

        consultaSQL = '''
                        SELECT provincia.descripcion AS provincia, departamento.descripcion AS depto, anio, semana_epidemiologica, grupoetario.descripcion AS grupoEtario, MAX(cantidad) AS cant_max
                        FROM casos, departamento, provincia, grupoetario
                        WHERE id_grupoetario = grupoetario.id AND id_depto = departamento.id AND id_provincia = provincia.id AND provincia.descripcion LIKE '%a' AND cantidad > '10'
                        GROUP BY * 
                        HAVING cantidad = 'cant_max'
                        ORDER BY cantidad DESC, provincia ASC, departamento ASC, anio ASC, grupoEtario ASC
                      '''

        imprimirEjercicio(consigna,[casos,provincia],consultaSQL)



#-------------------------------------------------------------------------------------

# OUTER JOIN 

    if entrada == '3a':

        '''EJERCICCIO 3A'''

        consigna = 'Devolver un listado con los nombres de los deptos qu no tienen casos asociados'

        consultaSQL = '''
                        SELECT departamento.descripcion AS nombre_depto_sin_casos
                        FROM departamento
                        LEFT OUTER JOIN casos ON id_depto = departamento.id
                        WHERE casos.id IS NULL
                      '''

        imprimirEjercicio(consigna,[casos,departamento],consultaSQL)



#-------------------------------------------------------------------------------------


    if entrada == '3b':

        '''EJERCICCIO 3B'''

        consigna = 'Devolver un listado con los tipo evento que no tienen casos asociados'

        consultaSQL = '''
                        SELECT DISTINCT tipoevento.descripcion AS tipoevento_sin_casos
                        FROM tipoevento
                        LEFT OUTER JOIN casos ON id_tipoevento = tipoevento.id
                        WHERE casos.id IS NULL
                      '''

        imprimirEjercicio(consigna,[casos,tipoevento],consultaSQL)



#-------------------------------------------------------------------------------------


    if entrada == '4a':

        '''EJERCICCIO 4A'''

        consigna = 'Calcular la cantidad total de casos que hay en la tabla casos.'

        consultaSQL = '''
                        SELECT DISTINCT COUNT(*) AS cantidad_total_de_casos
                        FROM casos
                      '''

        imprimirEjercicio(consigna,[casos],consultaSQL)



#-------------------------------------------------------------------------------------


    if entrada == '4b':

        '''EJERCICCIO 4B'''

        consigna = 'Calcular la cantidad total de casos que hay en la tabla casos para cada año y cada tipo de caso. Presentar la información de la siguiente manera: descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso (ascendente) y año (ascendente).'

        consultaSQL = '''
                        SELECT tipoevento.descripcion, casos.anio, COUNT(*) AS cantidad_total
                        FROM casos, tipoevento
                        WHERE tipoevento.id = casos.id_tipoevento
                        GROUP BY descripcion, anio
                        ORDER BY descripcion ASC, anio ASC
                      '''

        imprimirEjercicio(consigna,[casos, tipoevento],consultaSQL)



#-------------------------------------------------------------------------------------


    if entrada == '4c':

        '''EJERCICCIO 4C'''

        consigna = 'Idem anterior solo año 2019'

        consultaSQL = '''
                        SELECT tipoevento.descripcion, casos.anio, COUNT(*) AS cantidad_total
                        FROM casos, tipoevento
                        WHERE tipoevento.id = casos.id_tipoevento AND anio = '2019'
                        GROUP BY descripcion, anio
                        ORDER BY descripcion ASC, anio ASC
                      '''

        imprimirEjercicio(consigna,[casos, tipoevento],consultaSQL)



#-------------------------------------------------------------------------------------


    if entrada == '4d':

        '''EJERCICCIO 4D'''

        consigna = 'Calcular la cantidad total de departamentos que hay por provincia. Presentar la información ordenada por código de provincia.'

        consultaSQL = '''
                        SELECT provincia.id, provincia.descripcion, count(*) AS cantidad_departamentos
                        FROM departamento
                        INNER JOIN provincia ON provincia.id = departamento.id_provincia
                        GROUP BY provincia.descripcion, provincia.id
                        ORDER BY provincia.id DESC
                      '''

        imprimirEjercicio(consigna,[provincia, departamento],consultaSQL)


#-------------------------------------------------------------------------------------


    if entrada == '4e':

        '''EJERCICCIO 4E'''

        consigna = 'Departamentos con menor cantidad de casos en 2019'

        consultaSQL = '''
                        SELECT DISTINCT departamento.descripcion AS departamento, sum(cantidad) AS cantidad_de_casos
                        FROM departamento
                        INNER JOIN casos ON casos.id_depto = departamento.id
                        WHERE anio = '2019'
                        GROUP BY departamento.descripcion
                        ORDER BY cantidad_de_Casos ASC
                      '''
        cantidad_de_casos_depto = sql^ consultaSQL

        consulta1SQL = '''
                        SELECT DISTINCT departamento
                        FROM cantidad_de_casos_depto AS cdc
                        WHERE cantidad_de_casos <= ALL (SELECT MIN(cdc.cantidad_de_casos)
                                                        FROM cantidad_de_casos_depto AS cdc
                                                        )
                       '''

        imprimirEjercicio(consigna,[casos, departamento, cantidad_de_casos_depto],consulta1SQL)



#-------------------------------------------------------------------------------------


    if entrada == '4f':

        '''EJERCICCIO 4F'''

        consigna = 'Departamentos con mayor cantidad de casos en 2020'

        consultaSQL = '''
                        SELECT DISTINCT departamento.descripcion AS departamento, sum(cantidad) AS cantidad_de_casos
                        FROM departamento
                        INNER JOIN casos ON casos.id_depto = departamento.id
                        WHERE anio = '2020'
                        GROUP BY departamento.descripcion
                        ORDER BY cantidad_de_Casos ASC
                      '''
        cantidad_de_casos_depto = sql^ consultaSQL

        consulta1SQL = '''
                        SELECT DISTINCT departamento
                        FROM cantidad_de_casos_depto AS cdc
                        WHERE cantidad_de_casos >= ALL (SELECT MAX(cdc.cantidad_de_casos)
                                                        FROM cantidad_de_casos_depto AS cdc
                                                        )
                       '''

        imprimirEjercicio(consigna,[casos, departamento, cantidad_de_casos_depto],consulta1SQL)


#-------------------------------------------------------------------------------------

    if entrada == '4g':
         
        '''EJERCICIO 4G'''

        consigna = 'promedio de casos por provincia y por año'

        consultaSQL = '''
                        SELECT DISTINCT provincia.descripcion AS provincia, casos.cantidad  AS cantidad
                        FROM provincia, departamento, casos
                        WHERE departamento.id_provincia = provincia.id AND casos.id_depto = departamento.id AND anio = '2019'
                      '''

        p_cant_2019 = sql^ consultaSQL

        consultaSQL2 = '''
                        SELECT DISTINCT provincia.descripcion AS provincia, casos.cantidad  AS cantidad
                        FROM provincia, departamento, casos
                        WHERE departamento.id_provincia = provincia.id AND casos.id_depto = departamento.id AND anio = '2020'
                      '''

        p_cant_2020 = sql^ consultaSQL2

        consultaSQL1 = '''
                        SELECT DISTINCT provincia, AVG(p_cant_2019.cantidad) AS promedio_casos_2019
                        FROM p_cant_2019 
                        GROUP BY provincia
                        '''
        result_2019 = sql^ consultaSQL1

        consultaSQL4 = '''
                        SELECT DISTINCT provincia, AVG(p_cant_2020.cantidad) AS promedio_casos_2020
                        FROM p_cant_2020
                        GROUP BY provincia
                        '''
        result_2020 = sql^ consultaSQL4

        consultaSQL3 = '''
                        SELECT DISTINCT result_2020.provincia, promedio_casos_2019, promedio_casos_2020
                        FROM result_2019
                        RIGHT OUTER JOIN result_2020 ON result_2019.provincia = result_2020.provincia
                        '''
                        

        imprimirEjercicio(consigna,[casos,departamento,provincia],consultaSQL3)


#-------------------------------------------------------------------------------------

    if entrada == '4h': 















# =============================================================================
# DEFINICION DE FUNCIÓN DE IMPRESIÓN EN PANTALLA
# =============================================================================
# Imprime en pantalla en un formato ordenado:
    # 1. Consigna
    # 2. Cada dataframe de la lista de dataframes de entrada
    # 3. Query
    # 4. Dataframe de salida
def imprimirEjercicio(consigna, listaDeDataframesDeEntrada, consultaSQL):
    
    print("\033[36m# -----------------------------------------------------------------------------\033[0m")
    print("\033[31m#CONSIGNA:\033[0m", consigna)
    print("\033[36m# -----------------------------------------------------------------------------\033[0m")
    print()
    for i in range(len(listaDeDataframesDeEntrada)):
        print("\033[31m#ENTRADA: \033[0m","0",i,sep='')
        print("\033[36m# --------------------\033[0m")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("\033[36m# -----------------------------------------------------------------------------\033[0m")
    print("\033[31m#SQL:\033[0m")
    print("\033[36m# -----------------------------------------------------------------------------\033[0m")
    print(consultaSQL)
    print()
    print("\033[36m# -----------------------------------------------------------------------------\033[0m")
    print("\033[31m#ConsultaSQL:\033[0m")
    print("\033[36m# -----------------------------------------------------------------------------\033[0m")
    print(sql^ consultaSQL)
    print()
    print("\033[36m# -----------------------------------------------------------------------------\033[0m")
    print("\033[36m# -----------------------------------------------------------------------------\033[0m")
    print()
    print()



                    
        


    
if __name__ == '__main__':
    main()


