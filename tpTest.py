import numpy as np
import matplotlib.pyplot as plt
A = np.array([[0.9,0.075,0.025],[0.15,0.8,0.05],[0.25,0.25,0.5]])
v = np.array([1,2,3])


# EJERCICIO 1

#Funciones auxiliares
def vector_aleatorio(n):
    v = np.random.random(n)   # armamos vector de dimension n con un numero aleatorio en cada componente
    return(v)


def rayleigh(A,v):
    autovalor = np.dot(v,A@v) / np.dot(v,v)   # formula del cociente de rayleigh
    return autovalor

# FUNCION PRINCIPAL

v = vector_aleatorio(len(A))

def estado(A,v,k):
    lista_autovalores = []  #declaramos lista de autovalores que devolvera el programa
    v1 = v
    for i in range(k):
        v=A@v         # calculamos A * v y se lo asignamos a v, esto se repetira k veces
        autovalor_i = rayleigh(A,v)     # usando la funcion rayleigh() le asignamos el autovalor al autovector de la iteracion actual
        lista_autovalores.append(autovalor_i)   # agregamos el autovalor al final de la lista

    return(lista_autovalores)




# EJERCICIO 2




#Los elementos generados tienen rango de valores: [0-1]

def generarA(n):
    A = np.random.rand(n,n)
    return(A)

# generar matriz tal que los elementos Bij son random y ademas Bij = Bji

def generarB(dimension):
    n = dimension
    matriz_random = np.random.rand(n,n)
    for i in range(n):
        for j in range(i,n):
            matriz_random[j,i] = matriz_random[i,j]
    return matriz_random         


# generar matriz igual a B pero en la diagonal sumar 100

def generarC(matriz):
    for i in range(len(matriz)):
        matriz[i,i] += 100
    return matriz


# generar matriz igual a B pero en la diagonal sumar 1000

def generarD(matriz):
    for i in range(len(matriz)):
        matriz[i,i] += 1000
    return matriz


# GENERO LAS MATRICES A, B, C, D, Y UN VECTOR DE DIMENSION 100 

n=100 #dimension

A = generarA(n) #matriz random
B = generarB(n) #matriz simetrica
C = generarC(B) #matriz B con diagonal+100
D = generarD(B) #matriz B con diagonal+1000

v = vector_aleatorio(n)

# ARMO LISTA DE AUTOVALORES PARA 100 ITERACIONES DEL METODO DE LA POTENCIA

k=100 #iteraciones

autovalores_A = estado(A,v,k)
autovalores_B = estado(B,v,k)
autovalores_C = estado(C,v,k)
autovalores_D = estado(D,v,k)

# ARMO LISTA DE 100 PUNTOS DEL 1 AL 100

iteraciones = np.linspace(1,100,k)

plt.subplot(2, 2, 1)
plt.plot(iteraciones,autovalores_A,color="black", linewidth=1.0, linestyle="-",label="matrizA")
plt.legend(loc='lower right')
plt.title('matriz A')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_A).min(),np.ma.masked_invalid(autovalores_A).max()])

plt.subplot(2, 2, 2)
plt.plot(iteraciones,autovalores_B,color="blue", linewidth=1.0, linestyle="-",label="matrizB")
plt.legend(loc='lower right')
plt.title('matriz B')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_B).min(),np.ma.masked_invalid(autovalores_B).max()])

plt.subplot(2, 2, 3)
plt.plot(iteraciones,autovalores_C,color="green", linewidth=1.0, linestyle="-",label="matrizB")
plt.legend(loc='lower right')
plt.title('matriz C')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_C).min(),np.ma.masked_invalid(autovalores_C).max()])

plt.subplot(2, 2, 4)
plt.plot(iteraciones,autovalores_D,color="red", linewidth=1.0, linestyle="-",label="matrizB")
plt.legend(loc='lower right')
plt.title('matriz D')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_D).min(),np.ma.masked_invalid(autovalores_D).max()])


#plt.xscale('log')
plt.show()










