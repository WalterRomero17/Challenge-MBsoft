#define si el producto es Prioritario
def esPrioritario(codigo):
    if codigo[0] in ['P','W']:
        return True
    else:
        return False

#verifica que el código
def verificar(codigo):
    codigoNumerico = codigo[4:9]#tomo solo la parte del String que corresponde al código Numérico
    while len(codigoNumerico) != 1:
        suma = 0
        for elemento in codigoNumerico:
            suma = suma + int(elemento)

        codigoNumerico = str(suma)

    if codigoNumerico == codigo[-1]:
        return True
    else:
        return False

#ordeno la lista usando el algoritmo "Bubble Sort"
def ordenar(listaCodigos):

    n = len(listaCodigos)
    for i in range(1, n):
        for j in range(n-i):
            if listaCodigos[j][0] > listaCodigos[j+1][0]:
                listaCodigos[j], listaCodigos[j+1] = listaCodigos[j+1], listaCodigos[j]

'''
Otra manera de realizar esta función seria:
def ordenar(listaCodigos):
    listaCodigos.sort()
'''

def main():

    lista =["DCR-88578-9","WGR-11111-5","PZT-45425-8","ERP-12458-7","CRM-78451-2","PQA-59713-7"]

    for codigo in lista:
        print("El código: ",codigo)

        if (esPrioritario(codigo)):
            print("El producto es prioridad")
        else:
            print("El producto No es prioridad")

        if (verificar(codigo)):
            print("El digito verificador es correcto")
        else:
            print("El digito verificador No es correcto")
        print("-----------------------------------------")

    print("Lista: ",lista)
    ordenar(lista)
    print("lista ordena: ", lista)

if __name__ == "__main__":
    main()

