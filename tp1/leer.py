import pandas as pd
import os
from inline_sql import sql
import chardet

with open('./localidades-censales.csv', 'rb') as f:
    tipo = chardet.detect(f.read())

with open('./padron-de-operadores-organicos-certificados.csv', 'rb') as f:
    tipo1 = chardet.detect(f.read())
    
localidades_censales = pd.read_csv('./localidades-censales.csv',encoding=tipo['encoding'])
w_median_depto_priv_clae2 = pd.read_csv('./w_median_depto_priv_clae2.csv')
padron_de_operadores_organicos_certificados = pd.read_csv('./padron-de-operadores-organicos-certificados.csv',encoding=tipo1['encoding'])
diccionario_clae2 = pd.read_csv('./diccionario_clae2.csv')
diccionario_cod_depto = pd.read_csv('./diccionario_cod_depto.csv')


localidades_censales.columns
w_median_depto_priv_clae2 = pd.read_csv('./w_median_depto_priv_clae2.csv')
padron_de_operadores_organicos_certificados = pd.read_csv('./padron-de-operadores-organicos-certificados.csv',encoding=tipo1['encoding'])
diccionario_clae2 = pd.read_csv('./diccionario_clae2.csv')
diccionario_cod_depto = pd.read_csv('./diccionario_cod_depto.csv')



