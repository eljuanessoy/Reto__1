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