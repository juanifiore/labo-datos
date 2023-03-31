import os
import pandas as pd
import numpy as np

archivo = 'EncuestaMovilidadRespuestas.csv'
ruta = '.'
fname = os.path.join(ruta,archivo)
df = pd.read_csv(fname)
columnas = df.columns
cantidad_transporte = df['¿Cuál es el transporte que utilizó hoy para llegar a Ciudad Universitaria? \n- En caso de utilizar más de uno responder en base al trayecto final.'].value_counts()
transporte_mas_usado = cantidad_transporte[0]


