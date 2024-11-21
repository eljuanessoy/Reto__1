def mayor_suma(lista):
    mayor_suma = lista[0] + lista[1]
    for i in range(1, len(lista)-1):
        siguiente_suma = lista[i] + lista[i+1]     
        if siguiente_suma > mayor_suma:
            mayor_suma = siguiente_suma
    
    return mayor_suma


if __name__ == "__main__":
    lista = []
    while True:
        numeros = input("Ingrese un número entero cualquiera (Vacío para terminar): ")
        if numeros == "":
            break
        numeros = int(numeros)
        lista.append(numeros)
    
    print("La mayor suma entre dos números consecutivos es ", mayor_suma(lista))