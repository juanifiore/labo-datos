'''
Guia sql, Laboratorio de datos
Tema dengue
Juan Igacio Fiore 259/22
'''

from inline_sql import sql
import pandas as pd
import os

def main():
    '''ARMO LOS CSV'''
    ruta = '/home/juani/Documentos/Facultad/3 LABORATORIO DE DATOS/labo-datos/csv'
    casos = pd.read_csv(os.path.join(ruta,'casos.csv'))
    tipo_evento = pd.read_csv(os.path.join(ruta,'tipoevento.csv'))
    departamento = pd.read_csv(os.path.join(ruta,'departamento.csv'))
    provincia = pd.read_csv(os.path.join(ruta,'provincia.csv'))
    grupo_etario = pd.read_csv(os.path.join(ruta,'grupoetario.csv'))

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
                        SELECT descripcion, id_provincia
                        FROM departamento
                        GROUP BY id_provincia
                        HAVING id_provincia = 54
                      '''

        imprimirEjercicio(consigna,[departamento],consultaSQL)


#---------------------------------------------------------------------------------

    if entrada == '1g':

        '''EJERCICIO 1G'''

        consigna = 'Listar los registros de la tabla departamento cuyo codigo de provincia es 54'

        consultaSQL = '''
                        SELECT descripcion, id_provincia
                        FROM departamento
                        GROUP BY id_provincia
                        HAVING id_provincia = 54
                      '''

        imprimirEjercicio(consigna,[departamento],consultaSQL)



#---------------------------------------------------------------------------------




# =============================================================================
# DEFINICION DE FUNCIÓN DE IMPRESIÓN EN PANTALLA
# =============================================================================
# Imprime en pantalla en un formato ordenado:
    # 1. Consigna
    # 2. Cada dataframe de la lista de dataframes de entrada
    # 3. Query
    # 4. Dataframe de salida
def imprimirEjercicio(consigna, listaDeDataframesDeEntrada, consultaSQL):
    
    print("# -----------------------------------------------------------------------------")
    print("# Consigna: ", consigna)
    print("# -----------------------------------------------------------------------------")
    print()
    for i in range(len(listaDeDataframesDeEntrada)):
        print("# Entrada 0",i,sep='')
        print("# -----------")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("# SQL:")
    print("# ----")
    print(consultaSQL)
    print()
    print("# Salida:")
    print("# -------")
    print(sql^ consultaSQL)
    print()
    print("# -----------------------------------------------------------------------------")
    print("# -----------------------------------------------------------------------------")
    print()
    print()



                    
        


    
if __name__ == '__main__':
    main()


