# -*- coding: utf-8 -*-
import random 

def maximo(a,b):
    if a < b:
        b = a
    return b

def dos_pertenece(lista):
    res = False
    for i in lista:
        if i == 2:
            res=True
    return res

def pertenece(lista, elem):
    res = False
    if elem in lista:
        res = True
    return res

def es_par(n):
    res = False
    if n%2 == 0:
        res = True
    return res

def mas_larga(lista1,lista2):
    larga = lista1
    if len(lista1) < len(lista2):
        larga = lista2
    return larga

def tachar_pares(lista):
    for i in range(0,len(lista)):
        if es_par(lista[i]):
            lista[i] = 'x'
    return lista
        
def cant_e(lista):
    res = 0
    for c in lista:
        if c == 'e':
            res += 1
    return res

def sumar_unos(lista):
    for i in range(0,len(lista)):
        lista[i] += 1
    return lista

def mezclar(cadena1, cadena2):
    long1 = len(cadena1)
    long2 = len(cadena2)
    longest = max(long1,long2)
    shortest = min(long1,long2)
    mixed_word = ''
    i = 0
    while i < shortest:
        mixed_word += cadena1[i] + cadena2[i] 
        i += 1
    if long1 < long2:  
        while i < longest:
            mixed_word += cadena2[i]
            i += 1
    else:
        while i < longest:
            mixed_word += cadena1[i]
            i += 1
    return mixed_word

def geringoso(palabra):
    silaba = ['pa','pe','pi','po','pu']
    vocales = ['a','e','i','o','u']
    papalapabrapa = ''
    l = len(palabra)
    for i in range(0,l):
        papalapabrapa = papalapabrapa + palabra[i]
        for j in range (0,5):
            if vocales[j] == palabra[i] and i < l-1 and palabra[i+1] not in vocales:
                papalapabrapa = papalapabrapa + silaba[j]
        if i == l-1 and palabra[i] in vocales:
            for j in range(0,5):
                if palabra[i] == vocales[j]:
                    papalapabrapa += silaba[j]
    return papalapabrapa

def dicc_geringoso(palabras):
    diccionario = {}
    for p in palabras:
       diccionario[p] = geringoso(p)
    return diccionario
        
def generala(n):
    tirada = []
    for i in range(n):
        r = random.randrange(1,7)
        tirada.append(r)
    return tirada



