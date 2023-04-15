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


def df_jacaranda():
    fname = os.path.join(ruta,archivo)
    df = pd.read_csv(fname) 
    filas_de_jacaranda = df['nombre_com'] == 'Jacarandá'
    df_jac = df[filas_de_jacaranda]
    return df_jac

def df_palo():
    fname = os.path.join(ruta,archivo)
    df = pd.read_csv(fname) 
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
    fname = os.path.join(ruta,archivo)
    df = pd.read_csv(fname) 
    return df[df['espacio_ve'] == parque].shape[0]

def df_parque(parque):
    fname = os.path.join(ruta,archivo)
    df = pd.read_csv(fname) 
    return df[df['espacio_ve'] == parque]
    
def nativos(parque):
    fname = os.path.join(ruta,archivo)
    df = pd.read_csv(fname) 
    df_p = df_parque(parque)
    return df_p.loc[:,'origen'].value_counts()['Nativo/Autóctono']

# ARBOLADO VEREDAS

archivo1 = 'arbolado-publico-lineal-2017-2018.csv'
ruta1 = '.'


def df_veredas():
    fname1 = os.path.join(ruta1,archivo1)
    df1 = pd.read_csv(fname1,low_memory=False)
    columnas_seleccionadas = ['nombre_cientifico','ancho_acera','diametro_altura_pecho','altura_arbol']
    df_ver = df1[columnas_seleccionadas]
    cantidad_especies = df_ver.loc[:,'nombre_cientifico'].value_counts()
    return df_ver


def df_especies():
    especies_seleccionadas = ['Tilia x moltkei','Jacaranda mimosifolia','Tipuana tipu']
    df_ver = df_veredas()
    return df_ver[df_ver['nombre_cientifico'].isin(especies_seleccionadas)]


def df_tipas_parques():
    fname = os.path.join(ruta,archivo)
    df = pd.read_csv(fname) 
    columnas_seleccionadas = ['nombre_cie','altura_tot','diametro']
    df_col = df[columnas_seleccionadas]
    especies_seleccionadas = ['Tilia viridis subsp. x moltkei','Jacarandá mimosifolia','Tipuana Tipu']
    return df_col[df_col['nombre_cie'].isin(especies_seleccionadas)]

def df_tipas_veredas():
    fname = os.path.join(ruta1,archivo1)
    df = pd.read_csv(fname,low_memory=False) 
    columnas_seleccionadas = ['nombre_cientifico','altura_arbol','diametro_altura_pecho']
    df_col = df[columnas_seleccionadas]
    especies_seleccionadas = ['Tilia x moltkei','Jacaranda mimosifolia','Tipuana tipu']
    return df_col[df_col['nombre_cientifico'].isin(especies_seleccionadas)]

df_parques = df_tipas_parques()
df_parques['ambiente'] = 'parque'
df_veredas = df_tipas_veredas()
df_veredas['ambiente'] = 'vereda'
df_parques.columns = df_veredas.columns
df_tipas = pd.concat([df_parques,df_veredas],ignore_index=True)

