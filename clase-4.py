import os
import inline_sql
import pandas as pd
import numpy as np

'''
archivo = 'EncuestaMovilidadRespuestas.csv'
ruta = '.'
fname = os.path.join(ruta,archivo)
df = pd.read_csv(fname)
columnas = df.columns
cantidad_transporte = df['¿Cuál es el transporte que utilizó hoy para llegar a Ciudad Universitaria? \n- En caso de utilizar más de uno responder en base al trayecto final.'].value_counts()
transporte_mas_usado = cantidad_transporte[0]

'''

archivo = 'arbolado-en-espacios-verdes.csv'
ruta = '.'
fname = os.path.join(ruta,archivo)
df = pd.read_csv(fname) 


def df_jacaranda():
    filas_de_jacaranda = df['nombre_com'] == 'Jacarandá'
    df_jac = df[filas_de_jacaranda]
    return df_jac

def df_palo():
    filas_de_palo = df['nombre_com'] == 'Palo borracho'
    df_palo = df[filas_de_palo]
    return df_palo

def calcular(df):
    cantidad_de_arboles = df.shape[0]
    altura_maxima = df['altura_tot'].max()
    altura_minima = df['altura_tot'].min()
    suma_alturas = df['altura_tot'].sum()
    altura_promedio = suma_alturas/cantidad_de_arboles
    diametro_maximo = df['diametro'].max()
    diametro_minimo = df['diametro'].min()
    suma_diam = df['diametro'].sum()
    diametro_promedio = suma_diam/cantidad_de_arboles
    print('Altura max: ',altura_maxima,'\nAltura min: ',altura_minima,'\nAltura promedio: ',altura_promedio,'\nDiametro max: ',diametro_maximo,'\nDiametro min: ',diametro_minimo,'\nDiametro promedio: ',diametro_promedio,'\n')

def cantidad_arboles(parque):
    return df[df['espacio_ve'] == parque].shape[0]

def df_parque(parque):
    return df[df['espacio_ve'] == parque]
    
def nativos(parque):
    df_p = df_parque(parque)
    return df_p.loc[:,'origen'].value_counts()['Nativo/Autóctono']

# ARBOLADO VEREDAS

archivo1 = 'arbolado-publico-lineal-2017-2018.csv'
ruta1 = '.'
fname1 = os.path.join(ruta,archivo)
df1 = pd.read_csv(fname)

def df_veredas():
    columnas = ['nombre_cientifico','ancho_acera','diametro_altura_pecho','altura_arbol']
    df_ver = df1[columnas]
    cantidad_especies = df_ver.loc[:,'nombre_cientifico'].value_counts()
    return cantidad_especies 
