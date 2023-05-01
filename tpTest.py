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
        Av=A@v         # calculamos A * v y se lo asignamos a Av
        v = Av / np.linalg.norm(Av,2)   #normalizamos Av
        autovalor_i = rayleigh(A,v)     # usando la funcion rayleigh() le asignamos el autovalor al autovector de la iteracion actual
        lista_autovalores.append(autovalor_i)   # agregamos el autovalor al final de la lista

    return(lista_autovalores)




# EJERCICIO 2




#Los elementos generados tienen rango de valores: [0-1]

def generarA(n):
    A = np.random.rand(n,n)
    for i in range(n):
        for j in range(n):
            A[i,j] = A[i,j] * np.random.randint(100)
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
    C = matriz.copy()
    for i in range(len(matriz)):
        C[i,i] += 100
    return C


# generar matriz igual a B pero en la diagonal sumar 1000

def generarD(matriz):
    D = matriz.copy()
    for i in range(len(matriz)):
        D[i,i] += 1000
    return D


# GENERO LAS MATRICES A, B, C, D, Y UN VECTOR DE DIMENSION 100 

n=100 #dimension

A = generarA(n) #matriz random
B = generarB(n) #matriz simetrica
C = generarC(B) #matriz B con diagonal+100
D = generarD(B) #matriz B con diagonal+1000

v = vector_aleatorio(n)

# ARMO LISTA DE AUTOVALORES PARA 100 ITERACIONES DEL METODO DE LA POTENCIA

k=100

autovalores_A = estado(A,v,k)
autovalores_B = estado(B,v,k)
autovalores_C = estado(C,v,k)
autovalores_D = estado(D,v,k)

# ARMO LISTA DE 100 PUNTOS DEL 1 AL 100

iteraciones = np.linspace(1,k,k)

plt.figure(figsize=(12,10), dpi=100)


plt.subplot(2, 2, 1)
plt.plot(iteraciones,autovalores_A,color="black", linewidth=1.0, linestyle="-",label="matrizA")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('autovalor aproximado')
plt.title('matriz A')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_A).min(),np.ma.masked_invalid(autovalores_A).max()])

plt.subplot(2, 2, 2)
plt.plot(iteraciones,autovalores_B,color="blue", linewidth=1.0, linestyle="-",label="matrizB")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('autovalor aproximado')
plt.title('matriz B')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_B).min(),np.ma.masked_invalid(autovalores_B).max()])

plt.subplot(2, 2, 3)
plt.plot(iteraciones,autovalores_C,color="green", linewidth=1.0, linestyle="-",label="matrizC")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('autovalor aproximado')
plt.title('matriz C')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_C).min(),np.ma.masked_invalid(autovalores_C).max()])

plt.subplot(2, 2, 4)
plt.plot(iteraciones,autovalores_D,color="red", linewidth=1.0, linestyle="-",label="matrizD")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('autovalor aproximado')
plt.title('matriz D')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_D).min(),np.ma.masked_invalid(autovalores_D).max()])


#plt.xscale('log')
#plt.grid(True)
plt.show()



# EJERCICIO 3

# PARTE A

def vector_error(M,autovalores_M):
    aM = abs(np.linalg.eigvals(A)).max()    #autovalor de la matriz M de mayor valor absoluto
    n = len(autovalores_M)  #cantidad de la lista de aproximacion de autovalores
    e = np.zeros(n) #vector de errores (inicializado con n ceros)
    for i in range(n):
        e[i] = np.log(abs(aM-autovalores_M[i]))
    return e

# GENERO VECTORES DE ERROR A CADA MATRIZ

eA = vector_error(A,autovalores_A)
eB = vector_error(B,autovalores_B)
eC = vector_error(C,autovalores_C)
eD = vector_error(D,autovalores_D)


# GENERO LOS GRAFICOS DE CADA VECTOR DE ERRORES RESPECTO A LAS ITERACIONES

plt.figure(figsize=(12,10), dpi=100)

plt.subplot(2, 2, 1)
plt.plot(iteraciones,eA,color="black", linewidth=1.0, linestyle="-",label="erroresA")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('error')
plt.title('errores A')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_A).min(),np.ma.masked_invalid(autovalores_A).max()])

plt.subplot(2, 2, 2)
plt.plot(iteraciones,eB,color="blue", linewidth=1.0, linestyle="-",label="erroresB")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('error')
plt.title('errores B')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_B).min(),np.ma.masked_invalid(autovalores_B).max()])

plt.subplot(2, 2, 3)
plt.plot(iteraciones,eC,color="green", linewidth=1.0, linestyle="-",label="erroresC")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('error')
plt.title('errores C')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_C).min(),np.ma.masked_invalid(autovalores_C).max()])

plt.subplot(2, 2, 4)
plt.plot(iteraciones,eD,color="red", linewidth=1.0, linestyle="-",label="erroresD")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('error')
plt.title('errores D')
#plt.axis([0,k,np.ma.masked_invalid(autovalores_D).min(),np.ma.masked_invalid(autovalores_D).max()])


#plt.xscale('log')
plt.show()


# PARTE B

#----------------------------------------------------------------------------------------------------

#FUNCION PARA OBTENER EL AUTOVALOR DE MAYOR MODULO 

def primer_autovalor(autovalores_M):
    a0 = sorted(autovalores_M,reverse=True)[0]  # ordeno la lista y obtengo el mayor autovalor
    an = sorted(autovalores_M,reverse=True)[-1]     # ordeno la lista y obtengo el menor autovalor
    if abs(a0) > abs(an):   # comparo valor absoluto de ambos para devolver el de mayor modulo
        return a0
    else:
        return an

# FUNCION PARA OBTENER EL SEGUNDO AUTOVALOR DE MAYOR MODULO, EN EL CASO QUE EL PRIMERO ESTE REPETIDO OMITIENDOLOS 

def segundo_autovalor(autovalores_M):
    autovalores_ordenados = sorted(np.array(autovalores_M),reverse=True)    # ordeno la lista de mayor a menor y la asigno a la variable
    a1 = primer_autovalor(autovalores_M)    # obtengo el autovalor de mayor modulo y lo asigno a a1
    while a1 in autovalores_ordenados:  # genero un ciclo para eliminar todas las repeticiones del autovalor con mayor modulo
        autovalores_ordenados.remove(a1)
    return primer_autovalor(autovalores_ordenados)  # luego de eliminarlo/s obtengo el autovalor de mayor modulo 

# FUNCION f(x) = 2 * log(y2/y1) * x * log(e

def f_y_x(x,y1,y2):
    return 2*np.log10(abs(y2/y1))*x+np.log10(abs(eA[0]))

# GENERO GRAFICOS DE LA FUNCION ERROR

plt.figure(figsize=(12,10), dpi=100)

# funcion error matriz A

plt.subplot(4, 2, 1)
plt.plot(iteraciones,eA,color="black", linewidth=1.0, linestyle="-",label="erroresA")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('error')
plt.title('errores A')

# funcion error matriz B

plt.subplot(4, 2, 3)
plt.plot(iteraciones,eB,color="black", linewidth=1.0, linestyle="-",label="erroresB")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('error')
plt.title('errores A')

# funcion error matriz C

plt.subplot(4, 2, 5)
plt.plot(iteraciones,eC,color="black", linewidth=1.0, linestyle="-",label="erroresC")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('error')
plt.title('errores A')

# funcion error matriz D

plt.subplot(4, 2, 7)
plt.plot(iteraciones,eD,color="black", linewidth=1.0, linestyle="-",label="erroresD")
plt.legend(loc='lower right')
plt.xlabel('iteracion')
plt.ylabel('error')
plt.title('errores A')


# GENERO GRAFICOS DE LA RECTA APROXIMADA A CADA GRAFICO DE ERROR

x = iteraciones


y1A = primer_autovalor(autovalores_A)
y2A = segundo_autovalor(autovalores_A)
plt.subplot(4,2,2)
plt.plot(x, [f_y_x(i,y1A,y2A) for i in x]) 


y1B = primer_autovalor(autovalores_B)
y2B = segundo_autovalor(autovalores_B)
plt.subplot(4,2,4)
plt.plot(x, [f_y_x(i,y1B,y2B) for i in x]) 


y1C = primer_autovalor(autovalores_C)
y2C = segundo_autovalor(autovalores_C)
plt.subplot(4,2,6)
plt.plot(x, [f_y_x(i,y1C,y2C) for i in x]) 


y1D = primer_autovalor(autovalores_D)
y2D = segundo_autovalor(autovalores_D)
plt.subplot(4,2,8)
plt.plot(x, [f_y_x(i,y1D,y2D) for i in x]) 
plt.show()


'''
x = np.linspace(1,100,100)
y = np.zeros(100)
i = 1
y1 = primer_autovalor(autovalores_A)
y2 = segundo_autovalor(autovalores_A)
while i < 100:
    y[i] = 2*np.log(y2/y1)*x[i]+np.log(eA[0])
    i+=1

plt.plot(x,y)
plt.show()
'''











''' 
def graficar_aprox_autovalores(iteraciones):
    k=iteraciones

    autovalores_A = estado(A,v,k)
    autovalores_B = estado(B,v,k)
    autovalores_C = estado(C,v,k)
    autovalores_D = estado(D,v,k)

    # ARMO LISTA DE 100 PUNTOS DEL 1 AL 100

    iteraciones = np.linspace(1,k,k)

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

graficar_aprox_autovalores(100)
'''
