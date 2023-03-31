import numpy as np
import pandas as pd

def pisar_elemento(M,e):
    for i in range(len(M)):
        for j,x in enumerate(M[i]):
            if M[i,j] == e:
                M[i,j] = -1
    return M

# PANDA

def generar_serie_lista(data,tipo):
    s = pd.Series(data,dtype=tipo)
    return s

def generar_serie_dicc(data):
    print('desea ingresar indices? (s/n)')
    sn = input()
    if sn == 's':
        print('ingrese indices')
        indices = input()
        s = pd.Series(data,index=indices)
    else:
        s = pd.Series(data)
    return s
