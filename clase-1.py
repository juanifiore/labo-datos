"""def pila(altura_obelisco):
    altura_billete = 0.11 / 1000
    altura_obelisco = 67.5
    altura_pila = altura_billete
    dias = 1
    while altura_pila < altura_obelisco:
        altura_pila *= 2
        dias += 1
     print("Se nececitan {dias} dias para alcanzar la altura de {altura-obelisco}")

pila(altura_obelisco)
""" 

altura_billete = 0.11 / 1000
altura_obelisco = 67.5
altura_pila = altura_billete
dias = 1

def pila(altura_obelisco):
    for i in range(10000):
        if altura_pila > altura_obelisco:
            print("Se necesitan {dias} días para alcanzar la altura de {altura_obelisco} metros.")
            break
        altura_pila *= 2
        dias += 1

pila(67)
        
