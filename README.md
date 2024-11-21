# Reto #1
By Juan Esteban Molina Rey (eljuanessoy)

### 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

Se definieron las funciones correspondientes a las cuatro operaciones básicas. Luego, se solicita al usuario que introduzca dos números y el signo de la operación que desea realizar. Mediante una estructura match y case, se muestra el resultado de la función asociada al signo proporcionado. Si el usuario ingresa un carácter no válido, se genera un mensaje de advertencia.

```python
def suma(a, b) -> float:
    return a + b
def resta(a, b) -> float:
    return a - b
def multiplicación(a, b) -> float:
    return (a * b)
def división(a, b) -> float:
    return(a / b)

if __name__=="__main__":
    a = float(input("Ingrese un número: "))
    b = float(input("Ingrese otro número: "))
    signo = str(input("Ingrese el signo de la operación a realizar: "))
    match signo:
        case "+":
            print("La suma de " + str(a) + " y " + str(b) + " es " + str(suma(a,b)))
        case "-":
            print("La resta de " + str(a) + " y " + str(b) + " es " + str(resta(a,b)))
        case "*":
            print("La multiplicación de " + str(a) + " y " + str(b) + " es " + str(multiplicación(a,b)))
        case "/":
            print("La división de " + str(a) + " y " + str(b) + " es " + str(división(a,b)))
        case _:
            print("Ingresa un signo de suma (+), resta (-), multiplicación (*), ó división (/)")
```

### 2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

En este punto, se utilizó un ciclo `for` para iterar sobre cada letra de la palabra. A través de los índices, se comparó la primera letra con la última, la segunda con la penúltima, y así sucesivamente, verificando que sean iguales en cada caso. Si todas las comparaciones resultan verdaderas, la función devuelve `True`, indicando que la palabra es un palíndromo; de lo contrario, devuelve `False`.

```python
def palindromo(palabra) -> str:
    for letra in range(len(palabra)):
        if palabra[letra] == palabra[len(palabra)-letra-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    palabra = str(input("Ingrese una palabra: "))
    if palindromo(palabra):
        print("La palabra ingresada es palindromo")
    else:
        print("La palabra ingresada no es palindromo")
```

### 3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

Se inicializa la variable `i` con el valor 2 y se incrementa iterativamente en 1 para verificar que el número no sea divisible por ningún elemento de la lista proporcionada. Esto implica que si el residuo de la división nunca es cero, el número es considerado primo. La verificación se realiza mediante un ciclo `for` que evalúa cada número en la lista mientras este sea menor que el cuadrado de `i`.

```python
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
```

### 4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

Primero, se inicializa la variable `mayor_suma` con la suma de los dos primeros elementos de la lista. Luego, se recorre la lista utilizando un índice para calcular la suma de elementos consecutivos, es decir, los elementos en las posiciones `i` y `i + 1`. Si la suma actual es mayor que la almacenada en `mayor_suma`, se actualiza esta última con el nuevo valor. Este proceso continúa hasta que se evalúan todos los pares consecutivos de números en la lista.

```python
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
```

### 5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

Se emplea un ciclo `for` anidado para comparar cada palabra de la lista con las demás. Si dos palabras son diferentes y, al ordenar sus letras con la función `sorted`, resultan idénticas (lo que indica que tienen las mismas letras en la misma cantidad), se consideran anagramas. En ese caso, ambas palabras se agregan a una lista llamada `lista_anagramas`.

```python
def anagrama(lista_palabras):
    lista_anagramas = []
    for palabra1 in lista_palabras:
        for palabra2 in lista_palabras:
            if palabra1 != palabra2 and sorted(palabra1) == sorted(palabra2):
                lista_anagramas.append(palabra1)
                lista_anagramas.append(palabra2)
    return lista_anagramas

if __name__ == "__main__":            
    lista_palabras = []
    while True:
        palabra = input("Ingrese una palabra cualquiera (Vacío para terminar): ")
        if palabra == "":
            break
        lista_palabras.append(palabra)
    
    anagramas = anagrama(lista_palabras)
    if anagramas:
        print("Las palabras que son anagramas entre sí son:", anagramas)
    else:
        print("No hay anagramas en la lista de palabras.")
```
