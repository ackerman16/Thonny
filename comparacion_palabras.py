def palabras(palabra1, palabra2):
    if (palabra1 == palabra2):
        return "Son palabras iguales"
    else:
        return "Son palabras distintas"
palabra1 = str(input("Dime una palabra "))
palabra2 = str(input("Dime otra palabra "))

print(palabras(palabra1, palabra2))