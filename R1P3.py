def numeros_primos(lista):
    for num in lista:
        if num <= 1:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
    return True

if __name__ == "__main__":
    lista = []
    lista_primos = []
    while True:
        numeros = input("Ingrese un número entero cualquiera (Vacío para terminar): ")
        if numeros == "":
            break
        numeros = int(numeros)
        lista.append(numeros)
    
    for num in lista:
        if numeros_primos([num]):
            lista_primos.append(num)
    
    if lista_primos:
        print("Los números primos en la lista ingresada son:", lista_primos)
    else:
        print("No hay números primos en la lista ingresada.")