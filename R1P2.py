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