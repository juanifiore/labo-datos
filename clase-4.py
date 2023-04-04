import os
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
    altura_promedio = altura_maxima/cantidad_de_arboles
