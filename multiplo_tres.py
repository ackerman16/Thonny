def multiplo3(numero):
    if (numero % 3 == 0):
        return "El número es múltiplo de 3"
    else:
        return "El número no es múltiplo de 3"
num = int(input("Dime un número "))
print(multiplo3(num))

